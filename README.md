# beli-api

Unofficial SDKs for the [Beli](https://beliapp.com) restaurant-ranking app, in TypeScript, Python, and Go. All three are generated from one hand-written OpenAPI 3.1 spec covering 140 operations.

[![License: MIT](https://img.shields.io/github/license/ProjectBarks/beli-api)](LICENSE)
[![validate](https://img.shields.io/github/actions/workflow/status/ProjectBarks/beli-api/validate.yml?branch=main&label=validate)](https://github.com/ProjectBarks/beli-api/actions/workflows/validate.yml)
[![GitHub stars](https://img.shields.io/github/stars/ProjectBarks/beli-api?style=social)](https://github.com/ProjectBarks/beli-api)

> Not affiliated with, endorsed by, or supported by Beli. Reverse-engineered from observed traffic, so it may break without notice. You use your own account credentials at your own risk.

## Install

Nothing is on npm, PyPI, or pkg.go.dev yet. Clone the repo and use the SDKs from `sdks/`.

```bash
git clone https://github.com/ProjectBarks/beli-api
cd beli-api && npm install
```

## Quickstart

Log in and call any of the 140 operations. Headers, host routing, bearer tokens, refresh, and request spacing are handled for you.

### TypeScript

```ts
import { createBeliClient } from "beli-api-ts/beli";

const beli = await createBeliClient({ email, password });

const me = await beli.getLoggedIn();
const { data } = await beli.searchApp({ query: { term: "coffee", city: "New York, NY" } });
```

### Python

```python
from beli_api.beli import connect
from beli_api.api.search import search_app

beli = connect(email, password)
results = search_app.sync(client=beli, term="coffee", city="New York, NY")
```

### Go

```go
beli, err := beliapi.Connect(ctx, beliapi.Options{Email: email, Password: password})

term := "coffee"
res, err := beli.SearchAppWithResponse(ctx, &beliapi.SearchAppParams{Term: &term})
```

## What the client does for you

The API rejects anything that does not look like a browser, answering `403 {"detail":"You do not have permission to perform this action."}` when the `User-Agent` header is missing. Each client picks a realistic browser user agent at random and sends it with `Origin` on every request, so there is nothing to configure.

Override it if you want a specific fingerprint, or a bigger pool from a package like [`user-agents`](https://www.npmjs.com/package/user-agents) or [`fake-useragent`](https://pypi.org/project/fake-useragent/):

```ts
await createBeliClient({ email, password, userAgent: new UserAgent().toString() });
```

```python
connect(email, password, user_agent=UserAgent().random)
```

```go
beliapi.Connect(ctx, beliapi.Options{Email: email, Password: password, UserAgent: ua})
```

Also handled: operations are routed to the right one of the four hosts, requests are spaced 350 ms apart because the API throttles bursts, and expired access tokens are refreshed before the call goes out.

## Authentication

`POST /api/token/` takes `{email, password}` (`phone_no` works instead of `email`) and returns a token pair. There is no API key or app secret.

| Token | Lifetime | Notes |
|---|---|---|
| access | 20 minutes | sent as `Authorization: Bearer <token>` |
| refresh | 7 days | not rotated, so the same one works all week |

Access tokens are renewed for you before any request that would otherwise go out with an expired one, using the refresh token if it is still good and falling back to the password if it is not.

### Resuming without a password

Store the refresh token and reuse it for up to 7 days. No password, no login round trip.

```ts
const beli = await createBeliClient({ email, password });
save(beli.tokens.refresh);

// later
const beli = await createBeliClient({ refreshToken: load() });
```

```python
session = BeliSession(email=email, password=password)
beli = session.client()
save(session.tokens.refresh)

# later
session = BeliSession(refresh_token=load())
beli = session.client()
```

```go
s, _ := beliapi.NewSession(beliapi.Options{Email: email, Password: password})
beli, _ := s.Client(beliapi.HostAPI)
save(s.Tokens().Refresh)

// later
s, _ := beliapi.NewSession(beliapi.Options{RefreshToken: load()})
beli, _ := s.Client(beliapi.HostAPI)
```

Once both tokens are dead and no password is available, the client raises rather than failing silently on the next call.

Expect `/api/followers/` and `/api/average-score/` to return 503 intermittently, and note that rapid repeated logins are throttled.

## Coverage

140 operations across 137 endpoints and 4 hosts. The spec at [`openapi/beli.yaml`](openapi/beli.yaml) is the source of truth.

| Module | Ops | | Module | Ops |
|---|---|---|---|---|
| Business detail | 22 | | Lists and challenges | 12 |
| Profile and settings | 21 | | Feed | 11 |
| Social graph | 18 | | Notifications | 11 |
| Search and discovery | 13 | | Reservations | 7 |
| Ranking and bookmarks | 12 | | Auth and session | 5 |
| Telemetry | 3 | | Payments | 2 |

## Development

```bash
make sdks                    # regenerate all three SDKs from the spec
npm run validate:spec        # lint + bundle + operation count
cd validation && npx vitest run
```

Editing `openapi/beli.yaml` is the only way to change the generated code. The generators are [`@hey-api/openapi-ts`](https://github.com/hey-api/openapi-ts), [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client), and [`oapi-codegen`](https://github.com/oapi-codegen/oapi-codegen).

The convenience layers are hand-written and safe to edit: `sdks/typescript/beli.ts`, `sdks/go/beli.go`, and `sdkgen/python/beli.py` (copied into the Python package after each generation, since that generator rewrites its whole output directory).

Tests run offline by default. Set `BELI_EMAIL`, `BELI_PASSWORD`, `BELI_TEST_TARGET_USER`, and `BELI_TEST_TARGET_BUSINESS` to also run the live tests against the real API. Writes are tested in reversible pairs (follow then unfollow, bookmark then remove, rank then delete), each cleaned up in a `finally` block. CI logs in once per run and only tests operations whose spec entries changed in the diff.

## License

MIT
