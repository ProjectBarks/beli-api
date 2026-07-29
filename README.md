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

Two headers are mandatory on every request. Without `Origin` **and** a browser-like `User-Agent`, the backend replies `403 {"detail":"You do not have permission to perform this action."}`.

### TypeScript

```ts
import { createClient } from "beli-api-ts/client";
import { login, searchApp } from "beli-api-ts";

const UA =
  "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148";
const ORIGIN = "capacitor://localhost";
const ONBOARD = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app";
const API = "https://backoffice-service-t57o3dxfca-nn.a.run.app";

const onboard = createClient({ baseUrl: ONBOARD });
onboard.interceptors.request.use((req) => {
  req.headers.set("User-Agent", UA);
  return req;
});

const { data: tokens } = await login({
  client: onboard,
  headers: { Origin: ORIGIN },
  body: { email: "you@example.com", password: process.env.BELI_PASSWORD! },
});

const api = createClient({ baseUrl: API });
api.interceptors.request.use((req) => {
  req.headers.set("User-Agent", UA);
  req.headers.set("Authorization", `Bearer ${tokens!.access}`);
  return req;
});

const { data } = await searchApp({
  client: api,
  headers: { Origin: ORIGIN },
  query: { term: "coffee", city: "New York, NY" },
});
```

### Python

```python
import os
from beli_api import Client, AuthenticatedClient
from beli_api.api.auth import login
from beli_api.api.search import search_app
from beli_api.models import LoginRequest

UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
ONBOARD = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app"
API = "https://backoffice-service-t57o3dxfca-nn.a.run.app"

anon = Client(base_url=ONBOARD, headers={"User-Agent": UA})
tokens = login.sync(client=anon, body=LoginRequest(
    email="you@example.com", password=os.environ["BELI_PASSWORD"]))

api = AuthenticatedClient(base_url=API, token=tokens.access, headers={"User-Agent": UA})
results = search_app.sync(client=api, term="coffee", city="New York, NY")
```

The Python SDK already defaults `Origin` on every generated call, so you only add the user agent.

### Go

```go
package main

import (
	"context"
	"net/http"
	"os"

	beliapi "github.com/ProjectBarks/beli-api/sdks/go"
)

const (
	ua      = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
	origin  = "capacitor://localhost"
	onboard = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app"
	apiHost = "https://backoffice-service-t57o3dxfca-nn.a.run.app"
)

func main() {
	ctx := context.Background()
	header := func(k, v string) beliapi.ClientOption {
		return beliapi.WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
			req.Header.Set(k, v)
			return nil
		})
	}

	auth, _ := beliapi.NewClientWithResponses(onboard, header("User-Agent", ua))
	email := "you@example.com"
	tok, _ := auth.LoginWithResponse(ctx,
		&beliapi.LoginParams{Origin: origin},
		beliapi.LoginJSONRequestBody{Email: &email, Password: os.Getenv("BELI_PASSWORD")})

	api, _ := beliapi.NewClientWithResponses(apiHost,
		header("User-Agent", ua),
		header("Authorization", "Bearer "+tok.JSON200.Access))

	term := "coffee"
	_, _ = api.SearchAppWithResponse(ctx, &beliapi.SearchAppParams{Origin: origin, Term: &term})
}
```

## Authentication

`POST /api/token/` takes `{email, password}` (it also accepts `phone_no` instead of `email`) and returns an access and refresh token. There is no API key or app secret.

| Token | Lifetime | Notes |
|---|---|---|
| access | 20 minutes | send as `Authorization: Bearer <token>` |
| refresh | 7 days | `POST /api/token/refresh/`, and it is not rotated on use |

Reuse the access token until it is close to expiry, then refresh. Only log in again once the refresh token itself has expired. Store tokens yourself and keep them out of version control.

There is no published rate limit. Keep requests to roughly one every 350 ms, and expect `/api/followers/` and `/api/average-score/` to return 503 intermittently.

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

Editing `openapi/beli.yaml` is the only way to change the SDKs. The generators are [`@hey-api/openapi-ts`](https://github.com/hey-api/openapi-ts), [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client), and [`oapi-codegen`](https://github.com/oapi-codegen/oapi-codegen).

The test suite runs offline by default. Set `BELI_EMAIL`, `BELI_PASSWORD`, `BELI_TEST_TARGET_USER`, and `BELI_TEST_TARGET_BUSINESS` to also run the live tests, which hit the real API. Writes are tested in reversible pairs (follow then unfollow, bookmark then remove, rank then delete), each cleaned up in a `finally` block. CI logs in once per run and only tests the operations whose spec entries changed in the diff.

## License

MIT
