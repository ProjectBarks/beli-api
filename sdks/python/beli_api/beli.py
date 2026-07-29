"""Hand-written convenience layer over the generated client.

`make sdk-py` regenerates the whole package, then copies this file back in, so
edit it here in `sdkgen/python/` rather than in `sdks/python/`.
"""

import base64
import json
import random
import time
from dataclasses import dataclass, field

import httpx

from .api.auth import login as _login
from .api.auth import refresh_token as _refresh_token
from .client import Client
from .models import LoginRequest, RefreshRequest

HOST_ONBOARD = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app"
HOST_API = "https://backoffice-service-t57o3dxfca-nn.a.run.app"
HOST_RECS = "https://backoffice-service-recs-t57o3dxfca-nn.a.run.app"
HOST_ACTIVITY = "https://activity-service-978733420956.northamerica-northeast1.run.app"

#: The backend answers 403 {"detail": "You do not have permission to perform this
#: action."} to anything that does not look like a browser, so one of these is
#: picked at random unless ``user_agent`` is given. Any realistic browser string
#: works, including one from a package such as ``fake-useragent``.
USER_AGENTS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 16; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.7827.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
]


def _claims(token: str) -> dict:
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(payload))


def is_expired(token: str | None, skew_seconds: int = 60) -> bool:
    """True once the token is within ``skew_seconds`` of expiring.

    Missing or unparseable tokens count as expired, so this doubles as a
    "needs renewing" check.
    """
    if not token:
        return True
    try:
        return _claims(token)["exp"] - skew_seconds <= time.time()
    except Exception:
        return True


@dataclass
class Tokens:
    access: str = ""
    refresh: str = ""


@dataclass
class BeliSession:
    """Holds credentials and tokens, renewing the access token as needed.

    Use this when you want the tokens back so you can store them:

        session = BeliSession(email=email, password=password)
        beli = session.client()
        save(session.tokens.refresh)      # good for 7 days

    Next run, skip the password entirely:

        session = BeliSession(refresh_token=load())
        beli = session.client()
    """

    email: str | None = None
    password: str | None = None
    access_token: str = ""
    refresh_token: str = ""
    user_agent: str | None = None
    tokens: Tokens = field(init=False)

    def __post_init__(self) -> None:
        self.tokens = Tokens(access=self.access_token, refresh=self.refresh_token)
        self.user_agent = self.user_agent or random.choice(USER_AGENTS)
        self._anon = Client(base_url=HOST_ONBOARD, headers={"User-Agent": self.user_agent})

    @property
    def user_id(self) -> str:
        """UUID of the logged-in user, read out of the access token."""
        return _claims(self.ensure_fresh())["user_id"]

    def ensure_fresh(self) -> str:
        """Renew the access token if needed and return it.

        Access tokens last 20 minutes. Refresh tokens last 7 days and are not
        rotated, so the same one keeps working all week.
        """
        if not is_expired(self.tokens.access):
            return self.tokens.access

        if not is_expired(self.tokens.refresh):
            result = _refresh_token.sync(
                client=self._anon, body=RefreshRequest(refresh=self.tokens.refresh)
            )
            if result is not None and getattr(result, "access", None):
                self.tokens.access = result.access
                return self.tokens.access

        if self.email and self.password:
            pair = _login.sync(
                client=self._anon, body=LoginRequest(email=self.email, password=self.password)
            )
            if pair is None or not getattr(pair, "access", None):
                raise RuntimeError("beli: login failed")
            self.tokens = Tokens(access=pair.access, refresh=pair.refresh)
            return self.tokens.access

        raise RuntimeError(
            "beli: no usable token. Pass email and password, a live access_token, "
            "or a refresh_token issued in the last 7 days."
        )

    def client(self, base_url: str = HOST_API) -> Client:
        """A client that refreshes the access token before each request."""
        self.ensure_fresh()
        return Client(
            base_url=base_url,
            headers={"User-Agent": self.user_agent},
            httpx_args={"auth": _RefreshingAuth(self)},
        )


class _RefreshingAuth(httpx.Auth):
    """Attaches a live bearer token to every request, renewing it first."""

    def __init__(self, session: BeliSession) -> None:
        self._session = session

    def sync_auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {self._session.ensure_fresh()}"
        yield request

    async def async_auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {self._session.ensure_fresh()}"
        yield request


def connect(
    email: str | None = None,
    password: str | None = None,
    *,
    access_token: str = "",
    refresh_token: str = "",
    user_agent: str | None = None,
    base_url: str = HOST_API,
) -> Client:
    """Log in (or resume from a token) and return a ready-to-use client.

        beli = connect(email, password)
        results = search_app.sync(client=beli, term="coffee")

    Pass ``refresh_token`` instead of a password to resume a session without
    logging in again. Use :class:`BeliSession` when you also need the tokens
    back so you can store them.
    """
    session = BeliSession(
        email=email,
        password=password,
        access_token=access_token,
        refresh_token=refresh_token,
        user_agent=user_agent,
    )
    return session.client(base_url=base_url)
