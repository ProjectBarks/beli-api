"""Hand-written convenience layer over the generated client.

`make sdk-py` regenerates the whole package, then copies this file back in, so
edit it here in `sdkgen/python/` rather than in `sdks/python/`.
"""

import random

from .api.auth import login
from .client import AuthenticatedClient, Client
from .models import LoginRequest

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


def connect(
    email: str | None = None,
    password: str | None = None,
    *,
    access_token: str | None = None,
    user_agent: str | None = None,
    base_url: str = HOST_API,
) -> AuthenticatedClient:
    """Log in (or reuse a token) and return a ready-to-use client.

        beli = connect(email, password)
        results = search_app.sync(client=beli, term="coffee")

    Pass ``access_token`` to skip the login round trip. The generated calls
    already default the required ``Origin`` header.
    """
    ua = user_agent or random.choice(USER_AGENTS)

    if access_token is None:
        if not email or not password:
            raise ValueError("pass either email and password, or access_token")
        anon = Client(base_url=HOST_ONBOARD, headers={"User-Agent": ua})
        tokens = login.sync(client=anon, body=LoginRequest(email=email, password=password))
        if tokens is None or not getattr(tokens, "access", None):
            raise RuntimeError("beli: login failed")
        access_token = tokens.access

    return AuthenticatedClient(base_url=base_url, token=access_token, headers={"User-Agent": ua})
