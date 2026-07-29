from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_hscroll_lists_placement_body import CreateUserHscrollListsPlacementBody
from ...models.create_user_hscroll_lists_placement_response_200 import CreateUserHscrollListsPlacementResponse200
from ...models.error_detail import ErrorDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateUserHscrollListsPlacementBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/user-hscroll-lists/placement/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateUserHscrollListsPlacementResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateUserHscrollListsPlacementResponse200.from_dict(response.json())

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
) -> Response[CreateUserHscrollListsPlacementResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserHscrollListsPlacementBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[CreateUserHscrollListsPlacementResponse200 | ErrorDetail]:
    """Record placement of horizontal-scroll list modules shown to a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserHscrollListsPlacementBody | Unset): Body not captured in reference
            traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserHscrollListsPlacementResponse200 | ErrorDetail]
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
    body: CreateUserHscrollListsPlacementBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> CreateUserHscrollListsPlacementResponse200 | ErrorDetail | None:
    """Record placement of horizontal-scroll list modules shown to a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserHscrollListsPlacementBody | Unset): Body not captured in reference
            traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserHscrollListsPlacementResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserHscrollListsPlacementBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[CreateUserHscrollListsPlacementResponse200 | ErrorDetail]:
    """Record placement of horizontal-scroll list modules shown to a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserHscrollListsPlacementBody | Unset): Body not captured in reference
            traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserHscrollListsPlacementResponse200 | ErrorDetail]
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
    body: CreateUserHscrollListsPlacementBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> CreateUserHscrollListsPlacementResponse200 | ErrorDetail | None:
    """Record placement of horizontal-scroll list modules shown to a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserHscrollListsPlacementBody | Unset): Body not captured in reference
            traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserHscrollListsPlacementResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
