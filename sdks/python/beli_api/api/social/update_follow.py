from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.follow_edge import FollowEdge
from ...models.update_follow_body import UpdateFollowBody
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateFollowBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/follow/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | FollowEdge | None:
    if response.status_code == 200:
        response_200 = FollowEdge.from_dict(response.json())

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
) -> Response[ErrorDetail | FollowEdge]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateFollowBody,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | FollowEdge]:
    """Unfollow (set unfollow_dt on a follow edge)

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateFollowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | FollowEdge]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateFollowBody,
    origin: str = "https://localhost",
) -> ErrorDetail | FollowEdge | None:
    """Unfollow (set unfollow_dt on a follow edge)

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateFollowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | FollowEdge
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateFollowBody,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | FollowEdge]:
    """Unfollow (set unfollow_dt on a follow edge)

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateFollowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | FollowEdge]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateFollowBody,
    origin: str = "https://localhost",
) -> ErrorDetail | FollowEdge | None:
    """Unfollow (set unfollow_dt on a follow edge)

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateFollowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | FollowEdge
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
