from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.paginated_results import PaginatedResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    query: str,
    *,
    page: int | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    params: dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/search/{uuid}/{query}/".format(
            uuid=quote(str(uuid), safe=""),
            query=quote(str(query), safe=""),
        ),
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
    uuid: UUID,
    query: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Search for users by query string, scoped to a requesting user

    Args:
        uuid (UUID):
        query (str):
        page (int | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        query=query,
        page=page,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    query: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Search for users by query string, scoped to a requesting user

    Args:
        uuid (UUID):
        query (str):
        page (int | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | PaginatedResults
    """

    return sync_detailed(
        uuid=uuid,
        query=query,
        client=client,
        page=page,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    query: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Search for users by query string, scoped to a requesting user

    Args:
        uuid (UUID):
        query (str):
        page (int | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        query=query,
        page=page,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    query: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Search for users by query string, scoped to a requesting user

    Args:
        uuid (UUID):
        query (str):
        page (int | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | PaginatedResults
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            query=query,
            client=client,
            page=page,
            origin=origin,
        )
    ).parsed
