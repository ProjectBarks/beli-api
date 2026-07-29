from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_ranking_request import AddRankingRequest
from ...models.add_ranking_response import AddRankingResponse
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: AddRankingRequest,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/add-ranking/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddRankingResponse | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = AddRankingResponse.from_dict(response.json())

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
) -> Response[AddRankingResponse | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AddRankingRequest,
    origin: str = "https://localhost",
) -> Response[AddRankingResponse | ErrorDetail]:
    """Create a rating/review (sentiment seed; Beli computes the displayed 0–10 score server-side)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (AddRankingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddRankingResponse | ErrorDetail]
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
    body: AddRankingRequest,
    origin: str = "https://localhost",
) -> AddRankingResponse | ErrorDetail | None:
    """Create a rating/review (sentiment seed; Beli computes the displayed 0–10 score server-side)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (AddRankingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddRankingResponse | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AddRankingRequest,
    origin: str = "https://localhost",
) -> Response[AddRankingResponse | ErrorDetail]:
    """Create a rating/review (sentiment seed; Beli computes the displayed 0–10 score server-side)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (AddRankingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddRankingResponse | ErrorDetail]
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
    body: AddRankingRequest,
    origin: str = "https://localhost",
) -> AddRankingResponse | ErrorDetail | None:
    """Create a rating/review (sentiment seed; Beli computes the displayed 0–10 score server-side)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (AddRankingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddRankingResponse | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
