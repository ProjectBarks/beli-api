from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.update_device_body import UpdateDeviceBody
from ...models.update_device_response_200 import UpdateDeviceResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    device_id: str,
    *,
    body: UpdateDeviceBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/device/{device_id}/".format(
            device_id=quote(str(device_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | UpdateDeviceResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateDeviceResponse200.from_dict(response.json())

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
) -> Response[ErrorDetail | UpdateDeviceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDeviceBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | UpdateDeviceResponse200]:
    """Update device attribution record (AppsFlyer); request body not captured

    Args:
        device_id (str):
        origin (str):  Default: 'https://localhost'.
        body (UpdateDeviceBody | Unset): Body not captured in reference traffic (AppsFlyer
            attribution fields).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | UpdateDeviceResponse200]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDeviceBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | UpdateDeviceResponse200 | None:
    """Update device attribution record (AppsFlyer); request body not captured

    Args:
        device_id (str):
        origin (str):  Default: 'https://localhost'.
        body (UpdateDeviceBody | Unset): Body not captured in reference traffic (AppsFlyer
            attribution fields).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | UpdateDeviceResponse200
    """

    return sync_detailed(
        device_id=device_id,
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDeviceBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | UpdateDeviceResponse200]:
    """Update device attribution record (AppsFlyer); request body not captured

    Args:
        device_id (str):
        origin (str):  Default: 'https://localhost'.
        body (UpdateDeviceBody | Unset): Body not captured in reference traffic (AppsFlyer
            attribution fields).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | UpdateDeviceResponse200]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDeviceBody | Unset = UNSET,
    origin: str = "https://localhost",
) -> ErrorDetail | UpdateDeviceResponse200 | None:
    """Update device attribution record (AppsFlyer); request body not captured

    Args:
        device_id (str):
        origin (str):  Default: 'https://localhost'.
        body (UpdateDeviceBody | Unset): Body not captured in reference traffic (AppsFlyer
            attribution fields).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | UpdateDeviceResponse200
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
