from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_filter_options_body import CreateFilterOptionsBody
from ...models.create_filter_options_response_200 import CreateFilterOptionsResponse200
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFilterOptionsBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/filter-options/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateFilterOptionsResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateFilterOptionsResponse200.from_dict(response.json())

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
) -> Response[CreateFilterOptionsResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFilterOptionsBody,
    origin: str = "https://localhost",
) -> Response[CreateFilterOptionsResponse200 | ErrorDetail]:
    """Available filter option values for the discovery query builder; body shape not fully captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateFilterOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFilterOptionsResponse200 | ErrorDetail]
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
    body: CreateFilterOptionsBody,
    origin: str = "https://localhost",
) -> CreateFilterOptionsResponse200 | ErrorDetail | None:
    """Available filter option values for the discovery query builder; body shape not fully captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateFilterOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFilterOptionsResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFilterOptionsBody,
    origin: str = "https://localhost",
) -> Response[CreateFilterOptionsResponse200 | ErrorDetail]:
    """Available filter option values for the discovery query builder; body shape not fully captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateFilterOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFilterOptionsResponse200 | ErrorDetail]
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
    body: CreateFilterOptionsBody,
    origin: str = "https://localhost",
) -> CreateFilterOptionsResponse200 | ErrorDetail | None:
    """Available filter option values for the discovery query builder; body shape not fully captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateFilterOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFilterOptionsResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
