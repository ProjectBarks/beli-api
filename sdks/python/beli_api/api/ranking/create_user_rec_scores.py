from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_rec_scores_body import CreateUserRecScoresBody
from ...models.create_user_rec_scores_response_200 import CreateUserRecScoresResponse200
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUserRecScoresBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/user-rec-scores/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateUserRecScoresResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateUserRecScoresResponse200.from_dict(response.json())

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
) -> Response[CreateUserRecScoresResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserRecScoresBody,
    origin: str = "https://localhost",
) -> Response[CreateUserRecScoresResponse200 | ErrorDetail]:
    """Compute/refresh recommendation scores for a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserRecScoresBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserRecScoresResponse200 | ErrorDetail]
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
    body: CreateUserRecScoresBody,
    origin: str = "https://localhost",
) -> CreateUserRecScoresResponse200 | ErrorDetail | None:
    """Compute/refresh recommendation scores for a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserRecScoresBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserRecScoresResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserRecScoresBody,
    origin: str = "https://localhost",
) -> Response[CreateUserRecScoresResponse200 | ErrorDetail]:
    """Compute/refresh recommendation scores for a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserRecScoresBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserRecScoresResponse200 | ErrorDetail]
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
    body: CreateUserRecScoresBody,
    origin: str = "https://localhost",
) -> CreateUserRecScoresResponse200 | ErrorDetail | None:
    """Compute/refresh recommendation scores for a user; request body not captured

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateUserRecScoresBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserRecScoresResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
