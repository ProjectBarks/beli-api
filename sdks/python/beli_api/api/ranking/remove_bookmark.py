from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bookmark_request import BookmarkRequest
from ...models.error_detail import ErrorDetail
from ...models.remove_bookmark_response_200 import RemoveBookmarkResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: BookmarkRequest,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/remove-bookmark/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | RemoveBookmarkResponse200 | None:
    if response.status_code == 200:
        response_200 = RemoveBookmarkResponse200.from_dict(response.json())

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
) -> Response[ErrorDetail | RemoveBookmarkResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BookmarkRequest,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | RemoveBookmarkResponse200]:
    """Remove a bookmark from a business. Verified live.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (BookmarkRequest): Body for /api/add-bookmark/ and /api/remove-bookmark/. Verified
            live.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | RemoveBookmarkResponse200]
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
    body: BookmarkRequest,
    origin: str = "https://localhost",
) -> ErrorDetail | RemoveBookmarkResponse200 | None:
    """Remove a bookmark from a business. Verified live.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (BookmarkRequest): Body for /api/add-bookmark/ and /api/remove-bookmark/. Verified
            live.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | RemoveBookmarkResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BookmarkRequest,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | RemoveBookmarkResponse200]:
    """Remove a bookmark from a business. Verified live.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (BookmarkRequest): Body for /api/add-bookmark/ and /api/remove-bookmark/. Verified
            live.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | RemoveBookmarkResponse200]
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
    body: BookmarkRequest,
    origin: str = "https://localhost",
) -> ErrorDetail | RemoveBookmarkResponse200 | None:
    """Remove a bookmark from a business. Verified live.

    Args:
        origin (str):  Default: 'https://localhost'.
        body (BookmarkRequest): Body for /api/add-bookmark/ and /api/remove-bookmark/. Verified
            live.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | RemoveBookmarkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
