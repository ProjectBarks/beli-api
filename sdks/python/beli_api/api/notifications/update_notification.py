from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.update_notification_body import UpdateNotificationBody
from ...models.update_notification_response_200 import UpdateNotificationResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: UpdateNotificationBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/notification/{id}/".format(
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
) -> ErrorDetail | UpdateNotificationResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateNotificationResponse200.from_dict(response.json())

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
) -> Response[ErrorDetail | UpdateNotificationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateNotificationBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | UpdateNotificationResponse200]:
    """Update a notification (e.g. mark read/dismissed); request body not fully captured

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateNotificationBody | Unset): Body not captured in reference traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | UpdateNotificationResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateNotificationBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | UpdateNotificationResponse200 | None:
    """Update a notification (e.g. mark read/dismissed); request body not fully captured

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateNotificationBody | Unset): Body not captured in reference traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | UpdateNotificationResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateNotificationBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | UpdateNotificationResponse200]:
    """Update a notification (e.g. mark read/dismissed); request body not fully captured

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateNotificationBody | Unset): Body not captured in reference traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | UpdateNotificationResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateNotificationBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | UpdateNotificationResponse200 | None:
    """Update a notification (e.g. mark read/dismissed); request body not fully captured

    Args:
        id (int):
        origin (str):  Default: 'https://localhost'.
        body (UpdateNotificationBody | Unset): Body not captured in reference traffic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | UpdateNotificationResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
