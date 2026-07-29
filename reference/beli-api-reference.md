# Beli API — Master Reference (consolidated)

**Unofficial, reverse-engineered.** Single authoritative index for the Beli restaurant-app backend.
Consolidates seven HAR captures (app **v9.8.1**, iOS, 2026-07-28) with two independent external
reverse-engineering efforts. Beli offers no compatibility guarantee — treat as a snapshot.

- **137 unique endpoints** across 4 hosts (132 API · 3 ONBOARD · 2 ACTIVITY).
- **24 write endpoints** (POST/PUT) — every core write is now observed live, including the full
  rating (review) create/delete flow, which is **self-reverting** (`add-ranking` → `delete-ranking`).
- Credentials/JWTs are redacted throughout (`<JWT>` / `<redacted>`); only structural JWT claims shown.

## Table of contents
1. [Hosts](#1-hosts)
2. [Required headers & transport](#2-required-headers--transport)
3. [Authentication](#3-authentication)
4. [Identifiers & the EAV field system](#4-identifiers--the-eav-field-system)
5. [Conventions](#5-conventions)
6. [Write endpoints (the important part)](#6-write-endpoints)
7. [Full endpoint catalogue (137)](#7-full-endpoint-catalogue)
8. [Data models](#8-data-models)
9. [External corroboration & sources](#9-external-corroboration--sources)
10. [Inferred / still-unseen](#10-inferred--still-unseen)
11. [Provenance](#11-provenance)

---

## 1. Hosts

All are Google Cloud Run (`server: Google Frontend`). Base URLs:

| Key | Base URL | Role |
|---|---|---|
| **ONBOARD** | `https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app` | Login, token refresh, `user/logged-in`, onboarding |
| **API** | `https://backoffice-service-t57o3dxfca-nn.a.run.app` | Everything else — the main surface |
| **RECS** | `https://backoffice-service-recs-t57o3dxfca-nn.a.run.app` | Recommendations (`/api/recs/{uuid}/`); mirrors many API routes. *External sources only; not in our captures.* |
| **ACTIVITY** | `https://activity-service-978733420956.northamerica-northeast1.run.app` | Analytics sink (`activity`, `api-error`) — fire-and-forget |

Media CDN: `https://photos2.beliapp.cloud` (Backblaze B2 behind `s3.us-east-005.backblazeb2.com`).
Note: `/api/token/refresh/` was observed on **API** in H4 but is documented on **ONBOARD** by external
sources — it appears to work on both.

## 2. Required headers & transport

Framework: **Django REST Framework** (confirmed by `allow` headers, `count/next/previous/results`
envelopes, `/api/<res>/` trailing-slash routing, `field__name` filter syntax). Client is a
Capacitor/Ionic iOS webview.

Every authenticated request carries:

```
Authorization: Bearer <access JWT>
Origin: capacitor://localhost         # REQUIRED — requests 403 without an Origin header
Accept: application/json
```

- **The `Origin` header is enforced** (external efforts confirm: missing Origin → 403). The app sends
  `capacitor://localhost`; the two external clients use `https://localhost` + `Referer: https://localhost/`.
  Any works; one must be present.
- No API key, client secret, request signing, or device attestation exists. The bearer token is the
  only credential. HARs captured cleanly through a MITM proxy → no effective cert pinning on the API host.
- CORS: `access-control-allow-credentials: true`, origin reflected. No rate-limit headers observed;
  community-polite interval is **≥350 ms** between requests. `/api/followers/` and `/api/average-score/`
  are known to intermittently **503** — treat as best-effort with fallbacks.

## 3. Authentication

SimpleJWT (`djangorestframework-simplejwt`). Flow:

### 3.1 Login — `POST {ONBOARD}/api/token/`
```jsonc
// request
{ "email": "<redacted>", "password": "<redacted>" }   // also accepts { "phone_no": "+1..." } (E.164)
// response
{ "access": "<JWT>", "refresh": "<JWT>" }
```
The login serializer accepts **either** `email` or `phone_no` as the identifier.

### 3.2 Refresh — `POST {ONBOARD|API}/api/token/refresh/`  ✅ observed (H4)
```jsonc
{ "refresh": "<JWT>" }   ->   { "access": "<JWT>" }
```
**Refresh is NOT rotated** — the same refresh token keeps working until its 7-day expiry.

### 3.3 Current user — `GET {ONBOARD}/api/user/logged-in/`
Returns `{ count, results: [ <full profile incl. email, phone_no, home_city, referrer, sessions> ] }`.

### 3.4 Token lifetimes (from decoded JWT `exp - iat`)
| Token | TTL | Claims |
|---|---|---|
| access | **1200 s (20 min)** | `token_type=access, user_id, jti, iat, exp` |
| refresh | **604800 s (7 days)** | `token_type=refresh, user_id, jti, iat, exp` |

A client should: reuse the cached access token until it's within ~60 s of expiry → then refresh →
if refresh is expired, re-login with credentials.

### 3.5 Session heartbeat — `PUT {API}/api/user/u/{uuid}/`
Sends `fcm_token`, `live_activity_token`, `sessions`, `last_login`, version/build; returns the full
user object. Behaves like a login-state sync, not auth per se.

## 4. Identifiers & the EAV field system

- **User** — UUID (`bd6fbeef-31f0-4836-9199-69836572e74c`).
- **Business** — integer PK (`7316`); also a Google `place_id` (`ChIJ…`). `/api/business/` accepts
  either `id` or `place_id` (get-or-create).
- **Notification / feed item** — integer PK; a rating event's `notification_id` doubles as its feed id.
- **Category** — 3-letter code: `RES` restaurant, `DES` dessert, `BAR` bar, `BAK` bakery, … set as
  `default_category`.

**Generic EAV layer** exposed directly via `*-sparse`, `datauser*`, `user-setting`, `*-params` routes.
`field` integer id ↔ `field_name` label, e.g. `11=NOTES`, `206=AVGBUSINESSSCORE`,
`150=PERMISSIONNOTIFYFOLLOW`, `151=PERMISSIONNOTIFYBOOKMARK`, `410=SEEN_EXPLAIN_FRIEND_RECS`,
`602=ACCESS_UNLOCKED_RES_SHARING`. Query strings leak Django ORM syntax (`field__name=`,
`notification__id=`, `username__iexact=`) → `django-filter` FilterSets; other lookups
(`__in`, `__gte`, `__icontains`) plausibly work but are unverified.

## 5. Conventions

- **Envelopes (five shapes coexist):** DRF paginated `{count,next,previous,results}`; bare
  `{results:[…]}`; bare list `[…]`; bare scalar (`5990`, `true`, `"<JWT>"`); and keyed objects
  (e.g. res-availability keyed by `"{biz}_{date}_{time}_…"`).
- **Trailing slashes are mandatory** (Django `APPEND_SLASH`).
- **Pagination param unknown** — every `next` seen was `null`; large lists are returned whole
  (`user-business-photos` = 1413 rows / 1.1 MB; `all-cities` = 390 KB). External clients session-cache
  rather than paginate. `/api/user/search/` accepts `?page=`. Treat pagination as **unverified**.
- **Feature-flag query params** gate response shape: `supports_*`, `version=9.8.1`, `multi_category`,
  `menu_vibes`, `include_followed`, `reversed`, `no_mv`, `num_vis`.
- **`Allow` header** on each response lists supported verbs — reveals writes the app never exercised.
- **Behavioral gotchas:** `/api/scores/{uuid}/` ignores query filters (fetch once, client-filter by
  `business_id`); `/api/get-ranking/` needs `user`+`category`, ignores `business`; `/api/business/`
  does not embed friend scores (fetch `/api/scores/` separately).

## 6. Write endpoints

All 24 POST/PUT endpoints. The core mutations:

### Rating / review — create & delete ✅ observed live (H5)
Three-step create sequence (all three sent on ranking a place):
```
POST {API}/api/add-ranking/            # the write; returns the ranking object
POST {API}/api/process-add-ranking/    # side effects; -> { clear_playlists, unlocked_playlist_access }
POST {API}/api/check-share-post-rank/  # value:null + share flags; -> { post_rank_popups:[] }
```
`add-ranking` / `process-add-ranking` body (identical):
```jsonc
{ "category":"RES", "user_id":"<uuid>", "business_id":84, "value":2.5,   // value = sentiment seed
  "tagged_users":[], "local_datetime":"2026-07-28T21:31:42.627Z", "utc_offset":240,
  "visit_dates":["2026-07-27"], "visit_date_on_rank":"2026-07-27", "rank_button_source":null,
  "overall_rank_count":1, /* + constant capability flags: version_supports_multi_category, … */ }
// -> { "results": { "id":173721961, "user", "business":{…full Business…}, "value", "category", … } }
```
Client sends only a **sentiment seed** (`value`); Beli computes the displayed **0–10 score server-side**
(first-ever ranking = 10.0). Capture the `results.id` — it's the ranking id for delete.

**Delete a ranking/review** (soft delete, note it's a **PUT** with empty body):
```
PUT {API}/api/delete-ranking/{user_uuid}/{ranking_id}/   {}   -> { guide_items_removed:bool }
```
→ The rating flow is therefore **self-reverting**: `add-ranking` (capture `results.id`) then
`delete-ranking/{user}/{id}/`.

### Note / written review text ✅ observed live (H5)
```
POST {API}/api/data-user-business-text-new/  { user, business, field_name:"NOTES", value:"Yum" }
  -> { status:"success", note_created:bool }
```

### Follow / unfollow ✅ observed (H4)
```
POST {API}/api/follow/        { follower, followed }  -> { id, status:"ACTIVE", … }
PUT  {API}/api/follow/{id}/   { unfollow_dt }          -> { id, status:"INACTIVE", … }
GET  {API}/api/follow/?follower=&followed=             -> { count, results }   # existing-edge check
```

### Bookmarks *(external: beli-mcp)*
```
POST {API}/api/add-bookmark/     PUT {API}/api/remove-bookmark/
```

### Settings (EAV write) ✅ observed
```
POST {API}/api/user-setting/   { user, field_name, value }  -> { user, field:{id,name,…}, value }
```

### Photos
```
POST/PUT {API}/api/user-business-photo/[{id}/]     # allow-header + beli-mcp; body not captured
```

### Other observed writes
`POST /api/user/list/` (batch user hydration `{ids:[uuid]}`), `POST /api/filter-list/` &
`POST /api/filter-options/` (filtered/trending discovery), `POST /api/passed-user-corr/{uuid}/`
(`{ids:[uuid]}` batch affinity), `POST /api/user-rec-scores/`, `POST /api/user-hscroll-lists/placement/`,
`POST /api/challenge-progress-share/{uuid}/`, `PUT /api/notification/{id}/`,
`PUT /api/user/u/{uuid}/` (heartbeat), `PUT /api/device/{deviceId}/` (AppsFlyer attribution),
`POST {ACTIVITY}/api/activity/` & `POST {ACTIVITY}/api/api-error/` (telemetry).

## 7. Full endpoint catalogue

137 endpoints, grouped by module. Host = ONBOARD / API / ACTIVITY. "First HAR" provenance:
`H0-biz` (business page), `H2-home` (home bootstrap), `H3-login` (login), `H4-deep` (deep session), `H5-rate` (rating a place + delete).
"Allowed verbs" is the server's `Allow` header — verbs beyond the observed method are unexercised writes.

<!-- BEGIN AUTOGENERATED CATALOGUE (scripts regenerate from HAR union) -->

### Auth & session (5)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 1 | PUT | API | `/api/device/{deviceId}/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 2 | POST | ONBOARD | `/api/token/` | POST, OPTIONS | H3-login |
| 3 | POST | API | `/api/token/refresh/` | POST, OPTIONS | H4-deep |
| 4 | GET | ONBOARD | `/api/user/logged-in/` | GET, POST, PUT, HEAD, OPTIONS | H3-login |
| 5 | PUT | API | `/api/user/u/{uuid}/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |

### Reservations (7)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 6 | GET | API | `/api/available-reservations/{uuid}/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 7 | GET | API | `/api/business-res-booked-list/` | GET, HEAD, OPTIONS | H2-home |
| 8 | POST | API | `/api/businesses-res-availability/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 9 | GET | API | `/api/res-priority-data/` | GET, HEAD, OPTIONS | H4-deep |
| 10 | GET | API | `/api/res-report-issue-options/` | GET, HEAD, OPTIONS | H4-deep |
| 11 | GET | API | `/api/reservation-posting/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 12 | GET | API | `/api/reservations-claimed-today/` | GET, HEAD, OPTIONS | H4-deep |

### Feed & newsfeed (11)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 13 | GET | API | `/api/agg-following-new/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 14 | GET | API | `/api/feed-alert/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 15 | GET | API | `/api/feed-item-data/` | GET, HEAD, OPTIONS | H2-home |
| 16 | GET | API | `/api/newsfeed-current/{uuid}/{id}/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 17 | GET | API | `/api/newsfeed-data/{uuid}/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 18 | GET | API | `/api/newsfeed-reaction/{uuid}/` | GET, PUT, HEAD, OPTIONS | H2-home |
| 19 | GET | API | `/api/newsfeed-user/{uuid}/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 20 | GET | API | `/api/profile-newsfeed-data/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 21 | GET | API | `/api/single-notification-data/{id}/` | GET, HEAD, OPTIONS | H5-rate |
| 22 | GET | API | `/api/your-newsfeed-data/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 23 | GET | API | `/api/your-newsfeed-reaction/{uuid}/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |

### Social graph (18)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 24 | GET | API | `/api/corr/{uuid}/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 25 | GET | API | `/api/follow-count/{uuid}/followers/` | GET, HEAD, OPTIONS | H2-home |
| 26 | GET | API | `/api/follow-count/{uuid}/following/` | GET, HEAD, OPTIONS | H2-home |
| 27 | GET | API | `/api/follow-requests/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 28 | GET/POST | API | `/api/follow/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 29 | PUT | API | `/api/follow/{id}/` | GET, POST, PUT, HEAD, OPTIONS | H4-deep |
| 30 | GET | API | `/api/followers/{uuid}/` | — *(503 in capture)* | H4-deep |
| 31 | GET | API | `/api/following/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 32 | GET | API | `/api/get-user-tag-suggestions/` | GET, HEAD, OPTIONS | H5-rate |
| 33 | GET | API | `/api/leaderboard/{uuid}/RANK/all_members/` | GET, HEAD, OPTIONS | H2-home |
| 34 | GET | API | `/api/mutual-bookmarks/{uuid},{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 35 | POST | API | `/api/passed-user-corr/{uuid}/` | POST, OPTIONS | H4-deep |
| 36 | GET | API | `/api/people-you-may-know-full/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 37 | GET | API | `/api/shared-meals/{uuid}/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 38 | GET | API | `/api/tagged-users/` | GET, HEAD, OPTIONS | H0-biz |
| 39 | GET | API | `/api/user-activity-subscriptions/{uuid}/{uuid}/` | GET, POST, HEAD, OPTIONS | H4-deep |
| 40 | POST | API | `/api/user/list/` | POST, OPTIONS | H0-biz |
| 41 | GET | API | `/api/user/search/{uuid}/{query}/` | GET, HEAD, OPTIONS | H4-deep |

### Ranking, scores & bookmarks (12)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 42 | POST | API | `/api/add-ranking/` | GET, POST, HEAD, OPTIONS | H5-rate |
| 43 | POST | API | `/api/check-share-post-rank/` | POST, OPTIONS | H5-rate |
| 44 | PUT | API | `/api/delete-ranking/{uuid}/{id}/` | GET, POST, PUT, HEAD, OPTIONS | H5-rate |
| 45 | GET | API | `/api/get-bookmark/` | GET, HEAD, OPTIONS | H2-home |
| 46 | GET | API | `/api/get-ranking/` | GET, HEAD, OPTIONS | H2-home |
| 47 | POST | API | `/api/process-add-ranking/` | POST, OPTIONS | H5-rate |
| 48 | GET | API | `/api/score-average/{uuid}/ALL/` | GET, HEAD, OPTIONS | H2-home |
| 49 | GET | API | `/api/user-field-count/{uuid}/BOOKMARKED/` | GET, HEAD, OPTIONS | H0-biz |
| 50 | GET | API | `/api/user-field-count/{uuid}/RANK/` | GET, HEAD, OPTIONS | H2-home |
| 51 | POST | API | `/api/user-rec-scores/` | POST, OPTIONS | H2-home |
| 52 | GET | API | `/api/user-scores-cached/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 53 | GET | API | `/api/user-scores/{uuid}/` | GET, HEAD, OPTIONS | H2-home |

### Business detail (22)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 54 | GET | API | `/api/bookmark-status/{uuid}/{id}/` | GET, HEAD, OPTIONS | H4-deep |
| 55 | GET | API | `/api/business-count-rated/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 56 | GET | API | `/api/business-friend-text/{uuid}/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 57 | GET | API | `/api/business-histogram-data/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 58 | GET | API | `/api/business-labels/` | GET, HEAD, OPTIONS | H2-home |
| 59 | GET | API | `/api/closedatauserbusinessboolean/` | GET, HEAD, OPTIONS | H5-rate |
| 60 | GET | API | `/api/countuserbusinessoccasion/{id}/` | GET, HEAD, OPTIONS | H4-deep |
| 61 | POST | API | `/api/data-user-business-text-new/` | POST, OPTIONS | H5-rate |
| 62 | GET | API | `/api/databusinessfloat-sparse/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 63 | GET | API | `/api/datauserbusinesstext-sparse/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 64 | GET | API | `/api/dish-rec/` | GET, HEAD, OPTIONS | H0-biz |
| 65 | GET | API | `/api/friends-bookmarked/{uuid}/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 66 | GET | API | `/api/rec-score/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 67 | GET | API | `/api/scores/{uuid}/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 68 | GET | API | `/api/static-maps-url/` | GET, HEAD, OPTIONS | H0-biz |
| 69 | GET | API | `/api/suggest-business-cuisine/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 70 | GET | API | `/api/suggest-business-price/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 71 | GET | API | `/api/tagged-users-on-business/{uuid}/{id}/` | GET, POST, HEAD, OPTIONS | H0-biz |
| 72 | GET | API | `/api/user-business-labels/` | GET, HEAD, OPTIONS | H2-home |
| 73 | GET | API | `/api/user-business-photo/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 74 | GET | API | `/api/user-business-photos/` | GET, HEAD, OPTIONS | H0-biz |
| 75 | GET | API | `/api/visit-dates-on-business/{uuid}/{id}/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |

### Search & discovery (13)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 76 | GET | API | `/api/all-cities/` | GET, HEAD, OPTIONS | H0-biz |
| 77 | GET | API | `/api/business-link/` | GET, HEAD, OPTIONS | H4-deep |
| 78 | GET | API | `/api/business/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 79 | GET | API | `/api/cuisine/all-cuisines/` | GET, HEAD, OPTIONS | H0-biz |
| 80 | GET | API | `/api/current-city/{uuid}/{coords}/` | GET, HEAD, OPTIONS | H2-home |
| 81 | GET | API | `/api/filter-configs/` | GET, HEAD, OPTIONS | H0-biz |
| 82 | POST | API | `/api/filter-list/` | POST, OPTIONS | H4-deep |
| 83 | POST | API | `/api/filter-options/` | POST, OPTIONS | H2-home |
| 84 | GET | API | `/api/popular-in-city/{uuid}/{city}/` | GET, HEAD, OPTIONS | H2-home |
| 85 | GET | API | `/api/published-list-cities/` | GET, HEAD, OPTIONS | H4-deep |
| 86 | GET | API | `/api/search-app/` | GET, HEAD, OPTIONS | H0-biz |
| 87 | GET | API | `/api/top-cities/` | GET, HEAD, OPTIONS | H4-deep |
| 88 | GET | API | `/api/trending/{uuid}/` | GET, HEAD, OPTIONS | H2-home |

### Lists, guides & challenges (12)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 89 | GET | API | `/api/challenge-join-config/` | GET, HEAD, OPTIONS | H2-home |
| 90 | POST | API | `/api/challenge-progress-share/{uuid}/` | GET, POST, HEAD, OPTIONS | H2-home |
| 91 | GET | API | `/api/my-featured-list-challenges/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 92 | GET | API | `/api/playlists/` | GET, HEAD, OPTIONS | H2-home |
| 93 | GET | API | `/api/published-list-item-new/` | GET, PUT, HEAD, OPTIONS | H0-biz |
| 94 | GET | API | `/api/published-list/` | GET, HEAD, OPTIONS | H0-biz |
| 95 | GET | API | `/api/published-list/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 96 | GET | API | `/api/short-list/{uuid}/` | GET, POST, HEAD, OPTIONS | H2-home |
| 97 | GET | API | `/api/user-guide-items-close/` | GET, HEAD, OPTIONS | H5-rate |
| 98 | GET | API | `/api/user-guide-items/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 99 | GET | API | `/api/user-guide/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 100 | POST | API | `/api/user-hscroll-lists/placement/` | POST, OPTIONS | H2-home |

### Notifications (11)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 101 | GET | API | `/api/app-notification/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 102 | GET | API | `/api/banner-notification/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 103 | GET | API | `/api/blocked-me/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 104 | GET | API | `/api/blocked/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 105 | GET | API | `/api/count-app-notification-unread/` | GET, HEAD, OPTIONS | H0-biz |
| 106 | GET | API | `/api/mark-read/{uuid}/` | GET, HEAD, OPTIONS | H4-deep |
| 107 | GET | API | `/api/muted/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 108 | GET | API | `/api/notification-comment-count/{id}/` | GET, HEAD, OPTIONS | H0-biz |
| 109 | GET | API | `/api/notification-reaction/` | GET, POST, PUT, HEAD, OPTIONS | H0-biz |
| 110 | PUT | API | `/api/notification/{id}/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 111 | GET | API | `/api/popup/{uuid}/` | GET, HEAD, OPTIONS | H2-home |

### Payments & external tokens (2)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 112 | GET | API | `/api/apple-maps-token/` | GET, HEAD, OPTIONS | H4-deep |
| 113 | GET | API | `/api/stripe-payment-methods/` | GET, PUT, HEAD, OPTIONS | H4-deep |

### Profile, settings & config (21)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 114 | GET | API | `/api/app-rank/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 115 | GET | API | `/api/check-user-settings/` | GET, HEAD, OPTIONS | H4-deep |
| 116 | GET | API | `/api/count-ranked-this-year/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 117 | GET | API | `/api/creator-subscribe/` | GET, POST, HEAD, OPTIONS | H2-home |
| 118 | GET | API | `/api/datauserinteger/` | GET, POST, HEAD, OPTIONS | H2-home |
| 119 | GET | API | `/api/glassfy-config/` | GET, HEAD, OPTIONS | H2-home |
| 120 | GET | API | `/api/has-contacts/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 121 | GET | API | `/api/invites-feature-progress/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 122 | GET | API | `/api/invites-remaining/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 123 | GET | API | `/api/number-params-before-user/` | GET, HEAD, OPTIONS | H4-deep |
| 124 | GET | API | `/api/number-params/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 125 | GET | API | `/api/profile-progress/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 126 | GET | API | `/api/sharesheet-config/` | GET, HEAD, OPTIONS | H2-home |
| 127 | GET | API | `/api/taste-profile-config/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 128 | GET | API | `/api/text-params-before-user/` | GET, HEAD, OPTIONS | H4-deep |
| 129 | GET | API | `/api/text-params/{uuid}/` | GET, HEAD, OPTIONS | H2-home |
| 130 | GET | API | `/api/trigger/` | GET, HEAD, OPTIONS | H2-home |
| 131 | GET/POST | API | `/api/user-setting/` | GET, POST, HEAD, OPTIONS | H2-home |
| 132 | GET | API | `/api/user/bio/` | GET, HEAD, OPTIONS | H2-home |
| 133 | GET | API | `/api/user/member/` | GET, POST, PUT, HEAD, OPTIONS | H2-home |
| 134 | GET | API | `/api/user/streak/` | GET, HEAD, OPTIONS | H2-home |

### Telemetry (3)

| # | Method(s) | Host | Path | Allowed verbs | First HAR |
|---|---|---|---|---|---|
| 135 | POST | ONBOARD | `/api/activity/` | POST, OPTIONS | H3-login |
| 136 | POST | ACTIVITY | `/api/activity/` | POST, OPTIONS | H4-deep |
| 137 | POST | ACTIVITY | `/api/api-error/` | POST, OPTIONS | H4-deep |

<!-- END AUTOGENERATED CATALOGUE -->

## 8. Data models

Observed shapes (fields may vary by feature flags):

- **User** — `id(uuid), first_name, last_name, full_name, username, created_dt, instagram_url,
  tiktok_url, photo, profile_photo, public, school, company, has_supper_club, has_vip,
  is_playlist_eligible`; extended profile adds `phone_no, email, home_city, bio, referrer,
  referral_link, sessions, reservation_priority, qr_code, following(bool in search)`.
- **Business** — `id, place_id, name, status, city, borough, lat, lng, price, price_key, neighborhood,
  country, website, phone_number, cuisines[], default_category, quick_link, tz, has_res_links,
  has_delivery_links, has_cover_photo, has_no_show_fee, reservation_venue_id, businesshours_set[],
  businessdistinction_set[], businessHoursConfig{}`.
- **BusinessHours** — `open_day, close_day, open_time, close_time`.
- **Score** — `user_id, business_id, value(float), category, num_visits, notification_id, sent_dt`;
  cached variant `{user_id, business_id, value, category, labels[]}`.
- **Photo (UserPhoto)** — `id, image, thumbnail, bb_image, bb_thumbnail, description, order,
  favorite_dish, created_dt, status, likes[uuid], user, business`.
- **PublishedList** — `id, title, description, cover_photo{}, ranked, category, quick_link,
  challenge_info{is_joined, progress, total, participant_count}, status`.
- **FeedItem** — `id, event_type(ADD|BOOKMARK|…), sent_dt, user1, title, body, business, category,
  score, num_visits, business_full{}`.
- **FollowEdge** — `id, request_dt, accept_dt, unfollow_dt, unaccept_dt, status(ACTIVE|INACTIVE),
  follower, followed`. **FollowCount** — bare integer.
- **ReservationOffer** — `id, user{}, business{}` + slot metadata; availability keyed by composite string,
  `reservation_platforms:{ "<biz>": {name: OPENTABLE|SEVENROOMS} }`.
- **Field (EAV)** — `id, name, display, table, category, is_filter`; **UserSetting** — `{user, field{}, value, start_dt, end_dt}`.

## 9. External corroboration & sources

Found via authenticated GitHub code search (key: the unique host slug `t57o3dxfca`). Two independent
efforts target the **same current host** and validate/extend our captures:

| Source | What | Value |
|---|---|---|
| [`jcjc-dev/beli-mcp`](https://github.com/jcjc-dev/beli-mcp) | MCP server + typed Zod contract, **live-verified v9.3.1** | Request/response bodies incl. the `add-ranking` write flow; confirms hosts, TTLs, `Origin` requirement, non-rotated refresh |
| [`mergd/belimaps`](https://github.com/mergd/belimaps) | Maps overlay; `openapi/beli.yaml`, `research/endpoints.md`, `hosts.ts` | OpenAPI spec against current host; behavioral notes (scores-don't-filter, ≥350 ms interval); revealed RECS host |
| [`tidbyt/community`](https://github.com/tidbyt/community/blob/main/apps/belifeed/beli_feed.star) `belifeed` | Pixel-display feed app | Confirms `newsfeed-old/{id}/?max_items=30`, `newsfeed-scores/{id}` |
| `krsi-dev/beliapp-restaurant-list-scraper`, `leoadberg/leo.adberg.com` | Legacy scrapers (`beli.cleverapps.io`) | Older backend gen; `/api/user/member`, `/api/rank-list/{id}`, `/api/corr/{a}/{b}` |

`beli-mcp`'s generated OpenAPI is the recommended seed for any SDK-generation work (e.g. Speakeasy).

## 10. Inferred / still-unseen

- **Pagination parameters** — unproven; every `next` was `null`. `/api/user/search/` takes `?page=`.
- **Photo upload body** (`POST /api/user-business-photo/`) — allow-header + external only; not captured.
- **`add-bookmark` / `remove-bookmark` bodies** — from beli-mcp, not our own traffic. (The rating
  create/delete flow IS now observed live — see §6.)
- **RECS host routes** — external only; `/api/recs/{uuid}/` documented, not captured here.
- Flaky server-side: `/api/followers/` (503 seen), `/api/average-score/` (500 per belimaps).

## 11. Provenance

Seven HAR captures (app v9.8.1, 2026-07-28):

| Tag | HAR | Session | Beli endpoints |
|---|---|---|---|
| H0-biz | `02-12-00` | Search + one business page | 33 |
| — | `02-23-28` | *Different app ("Trie") — excluded* | 0 |
| H1-tun | `18-07-20` | Pinned TLS tunnels only | 0 |
| H2-home | `18-26-24` | Logged-in home bootstrap | 62 |
| H3-login | `18-29-01` | Login (onboarding) | 3 |
| H4-deep | `20-57-41` | Deep session: profiles, follow/unfollow, search, filters | 101 templates |
| H5-rate | `21-31-56` | Rank a place (add-ranking flow) + delete-ranking + note write | +9 new |

Supporting docs: `docs/har-notes/` (per-HAR working notes), `docs/research/` (SimpleJWT/DRF/public-docs
briefs), `docs/reviews/` (accuracy + completeness/redaction audits). Regeneration inputs live in the
session scratchpad (`union_endpoints.json`, `catalogue_table.md`).
