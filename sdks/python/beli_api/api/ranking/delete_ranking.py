from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_ranking_body import DeleteRankingBody
from ...models.delete_ranking_response_200 import DeleteRankingResponse200
from ...models.error_detail import ErrorDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    id: int,
    *,
    body: DeleteRankingBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/delete-ranking/{uuid}/{id}/".format(
            uuid=quote(str(uuid), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteRankingResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = DeleteRankingResponse200.from_dict(response.json())

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
) -> Response[DeleteRankingResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
    body: DeleteRankingBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[DeleteRankingResponse200 | ErrorDetail]:
    """Soft-delete a rating/review (PUT with empty body)

    Args:
        uuid (UUID):
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (DeleteRankingBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRankingResponse200 | ErrorDetail]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
    body: DeleteRankingBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> DeleteRankingResponse200 | ErrorDetail | None:
    """Soft-delete a rating/review (PUT with empty body)

    Args:
        uuid (UUID):
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (DeleteRankingBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRankingResponse200 | ErrorDetail
    """

    return sync_detailed(
        uuid=uuid,
        id=id,
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
    body: DeleteRankingBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[DeleteRankingResponse200 | ErrorDetail]:
    """Soft-delete a rating/review (PUT with empty body)

    Args:
        uuid (UUID):
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (DeleteRankingBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRankingResponse200 | ErrorDetail]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
    body: DeleteRankingBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> DeleteRankingResponse200 | ErrorDetail | None:
    """Soft-delete a rating/review (PUT with empty body)

    Args:
        uuid (UUID):
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (DeleteRankingBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRankingResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            id=id,
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
