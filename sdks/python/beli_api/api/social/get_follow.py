from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.paginated_results import PaginatedResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    follower: UUID | Unset = UNSET,
    followed: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    params: dict[str, Any] = {}

    json_follower: str | Unset = UNSET
    if not isinstance(follower, Unset):
        json_follower = str(follower)
    params["follower"] = json_follower

    json_followed: str | Unset = UNSET
    if not isinstance(followed, Unset):
        json_followed = str(followed)
    params["followed"] = json_followed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/follow/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | PaginatedResults | None:
    if response.status_code == 200:
        response_200 = PaginatedResults.from_dict(response.json())

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
) -> Response[ErrorDetail | PaginatedResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    follower: UUID | Unset = UNSET,
    followed: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Existing-edge check between a follower and followed user

    Args:
        follower (UUID | Unset):
        followed (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        follower=follower,
        followed=followed,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    follower: UUID | Unset = UNSET,
    followed: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Existing-edge check between a follower and followed user

    Args:
        follower (UUID | Unset):
        followed (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | PaginatedResults
    """

    return sync_detailed(
        client=client,
        follower=follower,
        followed=followed,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    follower: UUID | Unset = UNSET,
    followed: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Existing-edge check between a follower and followed user

    Args:
        follower (UUID | Unset):
        followed (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        follower=follower,
        followed=followed,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    follower: UUID | Unset = UNSET,
    followed: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Existing-edge check between a follower and followed user

    Args:
        follower (UUID | Unset):
        followed (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | PaginatedResults
    """

    return (
        await asyncio_detailed(
            client=client,
            follower=follower,
            followed=followed,
            origin=origin,
        )
    ).parsed
