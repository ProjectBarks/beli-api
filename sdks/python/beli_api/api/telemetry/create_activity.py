from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_activity_body import CreateActivityBody
from ...models.create_activity_response_200 import CreateActivityResponse200
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: CreateActivityBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/activity/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateActivityResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateActivityResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorDetail.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateActivityResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateActivityBody,
    origin: str = "https://localhost",
) -> Response[CreateActivityResponse200 | ErrorDetail]:
    """Fire-and-forget analytics event sink. Reference §7 lists this path on both the ACTIVITY host (row
    136) and the ONBOARD host (row 135, observed during login, H3-login) — OpenAPI paths are host-
    agnostic and cannot be duplicated, so this single operation is modeled on the ACTIVITY host; it is
    also accepted on https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app during login.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateActivityResponse200 | ErrorDetail]
    """

    kwargs = _get_kwargs(
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateActivityBody,
    origin: str = "https://localhost",
) -> CreateActivityResponse200 | ErrorDetail | None:
    """Fire-and-forget analytics event sink. Reference §7 lists this path on both the ACTIVITY host (row
    136) and the ONBOARD host (row 135, observed during login, H3-login) — OpenAPI paths are host-
    agnostic and cannot be duplicated, so this single operation is modeled on the ACTIVITY host; it is
    also accepted on https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app during login.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateActivityResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateActivityBody,
    origin: str = "https://localhost",
) -> Response[CreateActivityResponse200 | ErrorDetail]:
    """Fire-and-forget analytics event sink. Reference §7 lists this path on both the ACTIVITY host (row
    136) and the ONBOARD host (row 135, observed during login, H3-login) — OpenAPI paths are host-
    agnostic and cannot be duplicated, so this single operation is modeled on the ACTIVITY host; it is
    also accepted on https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app during login.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateActivityResponse200 | ErrorDetail]
    """

    kwargs = _get_kwargs(
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateActivityBody,
    origin: str = "https://localhost",
) -> CreateActivityResponse200 | ErrorDetail | None:
    """Fire-and-forget analytics event sink. Reference §7 lists this path on both the ACTIVITY host (row
    136) and the ONBOARD host (row 135, observed during login, H3-login) — OpenAPI paths are host-
    agnostic and cannot be duplicated, so this single operation is modeled on the ACTIVITY host; it is
    also accepted on https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app during login.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateActivityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateActivityResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
