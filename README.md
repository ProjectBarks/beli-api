# beli-api

Unofficial **Beli API** client / SDK for the Beli restaurant-ranking app — TypeScript, Python, and Go, generated from a hand-written OpenAPI 3.1 spec.

[![License: MIT](https://img.shields.io/github/license/ProjectBarks/beli-api)](https://github.com/ProjectBarks/beli-api/blob/main/LICENSE)
[![validate](https://img.shields.io/github/actions/workflow/status/ProjectBarks/beli-api/validate.yml?branch=main&label=validate)](https://github.com/ProjectBarks/beli-api/actions/workflows/validate.yml)
[![GitHub stars](https://img.shields.io/github/stars/ProjectBarks/beli-api?style=social)](https://github.com/ProjectBarks/beli-api)

> Unofficial, community-maintained. Not affiliated with, endorsed by, or supported by Beli.
> Reverse-engineered from observed traffic; may break without notice. Use your own account
> credentials at your own risk.

## Why

[Beli](https://beliapp.com) (the restaurant-ranking / "food Letterboxd" app) has no public API. This
repo is a single hand-written **OpenAPI 3.1** spec — reverse-engineered from real app traffic and
cross-checked against independent community efforts — covering 137 endpoints across auth, search,
business detail, social graph, rankings, feed, lists, notifications, reservations, payments, and
telemetry. From that one spec, `make sdks` regenerates fully typed **TypeScript**, **Python**, and
**Go** clients, so you don't have to hand-roll HTTP calls or guess at request/response shapes.

## Quickstart

The packages are **not yet published** to npm / PyPI / pkg.go.dev — registry publishing is planned.
For now, use the generated SDKs directly from this repo (`sdks/typescript`, `sdks/python`, `sdks/go`).

Every authenticated request needs a bearer access token *and* an `Origin: https://localhost` header
(the backend 403s without it). Log in once with your email/password to get a token pair, then
configure the client to attach both automatically.

### TypeScript

```ts
import { client, login, searchApp } from "./sdks/typescript/src";

const ORIGIN = { Origin: "https://localhost" };

const { data: tokens } = await login({
  headers: ORIGIN,
  body: { email: "you@example.com", password: "hunter2" },
});

// bearer token is reused for every subsequent call made with this client
client.setConfig({ auth: () => tokens!.access });

const { data } = await searchApp({ headers: ORIGIN });
```

### Python

```python
from beli_api import AuthenticatedClient, Client
from beli_api.api.auth import login
from beli_api.api.search import search_app
from beli_api.models import LoginRequest

# the "Origin: https://localhost" header defaults automatically on every generated call
anon = Client(base_url="https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app")
tokens = login.sync(client=anon, body=LoginRequest(email="you@example.com", password="hunter2"))

client = AuthenticatedClient(
    base_url="https://backoffice-service-t57o3dxfca-nn.a.run.app",
    token=tokens.access,
)
results = search_app.sync(client=client)
```

### Go

```go
import (
    "context"
    "net/http"

    beliapi "github.com/ProjectBarks/beli-api/sdks/go"
)

email := "you@example.com"
onboard, _ := beliapi.NewClient("https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app")
resp, _ := onboard.Login(ctx, &beliapi.LoginParams{Origin: "https://localhost"},
    beliapi.LoginJSONRequestBody{Email: &email, Password: "hunter2"})
// decode resp.Body into beliapi.TokenPair -> access/refresh

api, _ := beliapi.NewClient(
    "https://backoffice-service-t57o3dxfca-nn.a.run.app",
    beliapi.WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
        req.Header.Set("Authorization", "Bearer "+accessToken)
        return nil
    }),
)
resp, _ = api.SearchApp(ctx, &beliapi.SearchAppParams{Origin: "https://localhost"})
```

> Registry publishing (npm / PyPI / pkg.go.dev) is planned.

## Features

| Feature | Detail |
|---|---|
| Auth & token lifecycle | Login with email/password; access tokens live 20 min and refresh tokens live 7 days (not rotated) — reuse the cached access token, refresh near expiry, re-login only once the refresh token itself expires |
| Endpoint coverage | 137 endpoints across 12 modules (auth, profile, search, business, social, ranking, feed, lists, notifications, reservations, payments, telemetry) |
| Languages | TypeScript, Python, Go — all generated from one OpenAPI 3.1 spec, kept in sync |
| Typed | Full request/response types (interfaces, Pydantic-style dataclasses, Go structs) — no hand-maintained model drift |
| Rate-limit courtesy | No documented server rate limit; SDKs default to a polite **~350 ms** interval between requests |
| CI | Change-tree-gated live validation — endpoint tests only run against the operations affected by a given diff |

## Endpoint coverage

137 endpoints, hand-cataloged from live traffic across 12 modules. Full detail, HTTP verbs, hosts, and
provenance live in [`openapi/beli.yaml`](openapi/beli.yaml) (and the human-readable
[endpoint catalogue](reference/beli-api-reference.md#7-full-endpoint-catalogue)).

| Module | Operations |
|---|---|
| Auth & session | 5 |
| Profile, settings & config | 21 |
| Search & discovery | 13 |
| Business detail | 22 |
| Social graph | 18 |
| Ranking, scores & bookmarks | 12 |
| Feed & newsfeed | 11 |
| Lists, guides & challenges | 12 |
| Notifications | 11 |
| Reservations | 7 |
| Payments & external tokens | 2 |
| Telemetry | 3 |
| **Total** | **137** |

## Authentication & credentials

There is no API key or app secret — the only credential is your Beli account's email/password,
exchanged for a JWT access/refresh pair via `POST /api/token/`. Access tokens last 20 minutes,
refresh tokens last 7 days and are **not rotated** on use. Store tokens yourself; never commit them.
Every request additionally requires an `Origin` header (`https://localhost` works; the official app
sends `capacitor://localhost`) or the backend returns `403`.

There's no published rate limit, but be a good citizen: keep requests to roughly one every **350 ms**
and avoid hammering endpoints known to intermittently `503` (e.g. `followers`, `average-score`).

## Contributing / regenerating the SDKs

The OpenAPI spec at [`openapi/beli.yaml`](openapi/beli.yaml) is the single source of truth. After
editing it, regenerate all three SDKs with:

```bash
make sdks
```

This runs `@hey-api/openapi-ts` (TypeScript), `openapi-python-client` (Python), and `oapi-codegen`
(Go) against the spec. `make validate` (see `.github/workflows/validate.yml`) lints the spec and, on
`main`, live-tests only the operations affected by the diff.

## Unverified / inferred

Most of this spec is corroborated by live HAR captures. A few pieces are not:

- `POST /api/token/refresh/` is confirmed observed live.
- `createBookmark` / `removeBookmark` (`/api/add-bookmark/`, `/api/remove-bookmark/`) are marked
  `x-beli-unverified: true` in the spec — their request bodies are inferred from an external
  community client (beli-mcp), not captured directly.
- The `RECS` host (`/api/recs/{uuid}/`, recommendations) is documented from external sources only —
  it never appeared in our own captures.

See [`reference/beli-api-reference.md`](reference/beli-api-reference.md) for full provenance.

---

**Keywords:** Beli API, Beli SDK, unofficial Beli API, Beli restaurant app API, reverse-engineered
API, restaurant ranking API, OpenAPI 3.1, TypeScript SDK, Python SDK, Go SDK, foodie app API,
Beli client library, REST API wrapper.
