from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.paginated_results import PaginatedResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    place_id: str | Unset = UNSET,
    from_business_page: bool | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    params: dict[str, Any] = {}

    params["id"] = id

    params["place_id"] = place_id

    params["from_business_page"] = from_business_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/business/",
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
    id: int | Unset = UNSET,
    place_id: str | Unset = UNSET,
    from_business_page: bool | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Look up (get-or-create) a business by internal id or Google place_id

    Args:
        id (int | Unset):
        place_id (str | Unset):
        from_business_page (bool | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        id=id,
        place_id=place_id,
        from_business_page=from_business_page,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    place_id: str | Unset = UNSET,
    from_business_page: bool | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Look up (get-or-create) a business by internal id or Google place_id

    Args:
        id (int | Unset):
        place_id (str | Unset):
        from_business_page (bool | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | PaginatedResults
    """

    return sync_detailed(
        client=client,
        id=id,
        place_id=place_id,
        from_business_page=from_business_page,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    place_id: str | Unset = UNSET,
    from_business_page: bool | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | PaginatedResults]:
    """Look up (get-or-create) a business by internal id or Google place_id

    Args:
        id (int | Unset):
        place_id (str | Unset):
        from_business_page (bool | Unset):
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | PaginatedResults]
    """

    kwargs = _get_kwargs(
        id=id,
        place_id=place_id,
        from_business_page=from_business_page,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    place_id: str | Unset = UNSET,
    from_business_page: bool | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | PaginatedResults | None:
    """Look up (get-or-create) a business by internal id or Google place_id

    Args:
        id (int | Unset):
        place_id (str | Unset):
        from_business_page (bool | Unset):
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
            id=id,
            place_id=place_id,
            from_business_page=from_business_page,
            origin=origin,
        )
    ).parsed
