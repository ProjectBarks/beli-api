package beliapi

// Hand-written convenience layer. `make sdk-go` only writes beliapi.gen.go, so
// this file survives regeneration.

import (
	"context"
	"fmt"
	"math/rand"
	"net/http"
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

// Options configures Connect. Supply Email and Password, or an AccessToken from
// an earlier session.
type Options struct {
	Email       string
	Password    string
	AccessToken string
	// UserAgent defaults to a random entry from UserAgents.
	UserAgent string
	// Origin defaults to DefaultOrigin.
	Origin string
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
	ua := o.UserAgent
	if ua == "" {
		ua = UserAgents[rand.Intn(len(UserAgents))]
	}
	origin := o.Origin
	if origin == "" {
		origin = DefaultOrigin
	}

	token := o.AccessToken
	if token == "" {
		if o.Email == "" || o.Password == "" {
			return nil, fmt.Errorf("beli: pass either Email and Password, or an AccessToken")
		}
		auth, err := NewClientWithResponses(HostOnboard, header("User-Agent", ua), header("Origin", origin))
		if err != nil {
			return nil, err
		}
		res, err := auth.LoginWithResponse(ctx,
			&LoginParams{Origin: OriginHeader(origin)},
			LoginJSONRequestBody{Email: &o.Email, Password: o.Password})
		if err != nil {
			return nil, err
		}
		if res.JSON200 == nil {
			return nil, fmt.Errorf("beli: login failed with status %s", res.HTTPResponse.Status)
		}
		token = res.JSON200.Access
	}

	return NewClientWithResponses(HostAPI,
		header("User-Agent", ua),
		header("Origin", origin),
		header("Authorization", "Bearer "+token))
}
