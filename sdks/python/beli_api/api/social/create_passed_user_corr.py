from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_passed_user_corr_body import CreatePassedUserCorrBody
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: CreatePassedUserCorrBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/passed-user-corr/{uuid}/".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | list[Any] | None:
    if response.status_code == 200:
        response_200 = cast(list[Any], response.json())

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
) -> Response[ErrorDetail | list[Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePassedUserCorrBody,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | list[Any]]:
    """Batch affinity/correlation lookup for a list of users

    Args:
        uuid (UUID):
        origin (str):  Default: 'https://localhost'.
        body (CreatePassedUserCorrBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | list[Any]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePassedUserCorrBody,
    origin: str = "https://localhost",
) -> ErrorDetail | list[Any] | None:
    """Batch affinity/correlation lookup for a list of users

    Args:
        uuid (UUID):
        origin (str):  Default: 'https://localhost'.
        body (CreatePassedUserCorrBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | list[Any]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePassedUserCorrBody,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | list[Any]]:
    """Batch affinity/correlation lookup for a list of users

    Args:
        uuid (UUID):
        origin (str):  Default: 'https://localhost'.
        body (CreatePassedUserCorrBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | list[Any]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePassedUserCorrBody,
    origin: str = "https://localhost",
) -> ErrorDetail | list[Any] | None:
    """Batch affinity/correlation lookup for a list of users

    Args:
        uuid (UUID):
        origin (str):  Default: 'https://localhost'.
        body (CreatePassedUserCorrBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | list[Any]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
