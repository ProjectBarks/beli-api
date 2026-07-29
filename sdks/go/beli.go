package beliapi

// Hand-written convenience layer. `make sdk-go` only writes beliapi.gen.go, so
// this file survives regeneration.

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"strings"
	"sync"
	"time"
)

const (
	HostOnboard  = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app"
	HostAPI      = "https://backoffice-service-t57o3dxfca-nn.a.run.app"
	HostRecs     = "https://backoffice-service-recs-t57o3dxfca-nn.a.run.app"
	HostActivity = "https://activity-service-978733420956.northamerica-northeast1.run.app"

	// DefaultOrigin can be any value, it only has to be present.
	DefaultOrigin = "capacitor://localhost"
)

// UserAgents holds realistic browser User-Agents. The backend answers
// 403 {"detail":"You do not have permission to perform this action."} to any
// client that does not look like a browser, so one of these is picked at random
// unless Options.UserAgent is set.
var UserAgents = []string{
	"Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
	"Mozilla/5.0 (Linux; Android 16; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.7827.91 Mobile Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
}

// Options configures Connect. Supply Email and Password, or a RefreshToken or
// AccessToken from an earlier session.
type Options struct {
	Email       string
	Password    string
	AccessToken string
	// RefreshToken resumes a session without logging in again. Refresh tokens
	// last 7 days and are not rotated, so the same one keeps working all week.
	RefreshToken string
	// UserAgent defaults to a random entry from UserAgents.
	UserAgent string
	// Origin defaults to DefaultOrigin.
	Origin string
}

// Tokens is the current token pair. Read it off a Session to store the refresh
// token between runs.
type Tokens struct {
	Access  string
	Refresh string
}

// Session renews the access token as needed. Connect builds one internally;
// use NewSession when you also want the tokens back.
type Session struct {
	opts   Options
	tokens Tokens
	auth   *ClientWithResponses
	mu     sync.Mutex
}

func claims(token string) (map[string]any, error) {
	parts := strings.Split(token, ".")
	if len(parts) < 2 {
		return nil, fmt.Errorf("malformed token")
	}
	raw, err := base64.RawURLEncoding.DecodeString(parts[1])
	if err != nil {
		return nil, err
	}
	var out map[string]any
	return out, json.Unmarshal(raw, &out)
}

// IsExpired reports whether the token is within a minute of expiring. Missing
// or unparseable tokens count as expired.
func IsExpired(token string) bool {
	c, err := claims(token)
	if err != nil {
		return true
	}
	exp, ok := c["exp"].(float64)
	if !ok {
		return true
	}
	return time.Now().Add(time.Minute).After(time.Unix(int64(exp), 0))
}

// NewSession prepares a session without performing any network call yet.
func NewSession(o Options) (*Session, error) {
	if o.UserAgent == "" {
		o.UserAgent = UserAgents[rand.Intn(len(UserAgents))]
	}
	if o.Origin == "" {
		o.Origin = DefaultOrigin
	}
	auth, err := NewClientWithResponses(HostOnboard,
		header("User-Agent", o.UserAgent), header("Origin", o.Origin))
	if err != nil {
		return nil, err
	}
	return &Session{
		opts:   o,
		tokens: Tokens{Access: o.AccessToken, Refresh: o.RefreshToken},
		auth:   auth,
	}, nil
}

// Tokens returns the current pair. Store Refresh to resume later.
func (s *Session) Tokens() Tokens {
	s.mu.Lock()
	defer s.mu.Unlock()
	return s.tokens
}

// UserID reads the logged-in user's UUID out of the access token.
func (s *Session) UserID(ctx context.Context) (string, error) {
	token, err := s.EnsureFresh(ctx)
	if err != nil {
		return "", err
	}
	c, err := claims(token)
	if err != nil {
		return "", err
	}
	id, _ := c["user_id"].(string)
	return id, nil
}

// EnsureFresh renews the access token if needed and returns it. Access tokens
// last 20 minutes; refresh tokens last 7 days and are not rotated.
func (s *Session) EnsureFresh(ctx context.Context) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if !IsExpired(s.tokens.Access) {
		return s.tokens.Access, nil
	}

	if !IsExpired(s.tokens.Refresh) {
		res, err := s.auth.RefreshTokenWithResponse(ctx,
			&RefreshTokenParams{Origin: OriginHeader(s.opts.Origin)},
			RefreshTokenJSONRequestBody{Refresh: s.tokens.Refresh})
		if err == nil && res.JSON200 != nil && res.JSON200.Access != "" {
			s.tokens.Access = res.JSON200.Access
			return s.tokens.Access, nil
		}
	}

	if s.opts.Email != "" && s.opts.Password != "" {
		res, err := s.auth.LoginWithResponse(ctx,
			&LoginParams{Origin: OriginHeader(s.opts.Origin)},
			LoginJSONRequestBody{Email: &s.opts.Email, Password: s.opts.Password})
		if err != nil {
			return "", err
		}
		if res.JSON200 == nil {
			return "", fmt.Errorf("beli: login failed with status %s", res.HTTPResponse.Status)
		}
		s.tokens = Tokens{Access: res.JSON200.Access, Refresh: res.JSON200.Refresh}
		return s.tokens.Access, nil
	}

	return "", fmt.Errorf("beli: no usable token. Pass Email and Password, a live " +
		"AccessToken, or a RefreshToken issued in the last 7 days")
}

// Client returns a client for host that renews the token before each request.
func (s *Session) Client(host string) (*ClientWithResponses, error) {
	return NewClientWithResponses(host,
		header("User-Agent", s.opts.UserAgent),
		header("Origin", s.opts.Origin),
		WithRequestEditorFn(func(ctx context.Context, req *http.Request) error {
			token, err := s.EnsureFresh(ctx)
			if err != nil {
				return err
			}
			req.Header.Set("Authorization", "Bearer "+token)
			return nil
		}))
}

func header(key, value string) ClientOption {
	return WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
		req.Header.Set(key, value)
		return nil
	})
}

// Connect logs in if needed and returns a client for the main API host with the
// required headers and bearer token already applied.
//
//	beli, _ := beliapi.Connect(ctx, beliapi.Options{Email: e, Password: p})
//	res, _ := beli.SearchAppWithResponse(ctx, &beliapi.SearchAppParams{Term: &term})
//
// Note that params still carry an Origin field because it is declared in the
// spec; leave it empty and this layer fills it in.
func Connect(ctx context.Context, o Options) (*ClientWithResponses, error) {
	session, err := NewSession(o)
	if err != nil {
		return nil, err
	}
	if _, err := session.EnsureFresh(ctx); err != nil {
		return nil, err
	}
	return session.Client(HostAPI)
}
