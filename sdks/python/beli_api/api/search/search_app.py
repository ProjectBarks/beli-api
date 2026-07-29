from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.search_app_response_200 import SearchAppResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    term: str | Unset = UNSET,
    city: str | Unset = UNSET,
    coords: str | Unset = UNSET,
    user: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    params: dict[str, Any] = {}

    params["term"] = term

    params["city"] = city

    params["coords"] = coords

    json_user: str | Unset = UNSET
    if not isinstance(user, Unset):
        json_user = str(user)
    params["user"] = json_user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/search-app/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | SearchAppResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchAppResponse200.from_dict(response.json())

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
) -> Response[ErrorDetail | SearchAppResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    term: str | Unset = UNSET,
    city: str | Unset = UNSET,
    coords: str | Unset = UNSET,
    user: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | SearchAppResponse200]:
    """Primary in-app search (businesses, users, lists)

    Args:
        term (str | Unset):
        city (str | Unset):
        coords (str | Unset):
        user (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | SearchAppResponse200]
    """

    kwargs = _get_kwargs(
        term=term,
        city=city,
        coords=coords,
        user=user,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    term: str | Unset = UNSET,
    city: str | Unset = UNSET,
    coords: str | Unset = UNSET,
    user: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | SearchAppResponse200 | None:
    """Primary in-app search (businesses, users, lists)

    Args:
        term (str | Unset):
        city (str | Unset):
        coords (str | Unset):
        user (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | SearchAppResponse200
    """

    return sync_detailed(
        client=client,
        term=term,
        city=city,
        coords=coords,
        user=user,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    term: str | Unset = UNSET,
    city: str | Unset = UNSET,
    coords: str | Unset = UNSET,
    user: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | SearchAppResponse200]:
    """Primary in-app search (businesses, users, lists)

    Args:
        term (str | Unset):
        city (str | Unset):
        coords (str | Unset):
        user (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | SearchAppResponse200]
    """

    kwargs = _get_kwargs(
        term=term,
        city=city,
        coords=coords,
        user=user,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    term: str | Unset = UNSET,
    city: str | Unset = UNSET,
    coords: str | Unset = UNSET,
    user: UUID | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | SearchAppResponse200 | None:
    """Primary in-app search (businesses, users, lists)

    Args:
        term (str | Unset):
        city (str | Unset):
        coords (str | Unset):
        user (UUID | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | SearchAppResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            term=term,
            city=city,
            coords=coords,
            user=user,
            origin=origin,
        )
    ).parsed
