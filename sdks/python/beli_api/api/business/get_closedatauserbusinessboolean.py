from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.get_closedatauserbusinessboolean_response_200 import GetClosedatauserbusinessbooleanResponse200
from ...types import Response


def _get_kwargs(
    *,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/closedatauserbusinessboolean/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDetail | GetClosedatauserbusinessbooleanResponse200 | None:
    if response.status_code == 200:
        response_200 = GetClosedatauserbusinessbooleanResponse200.from_dict(response.json())

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
) -> Response[ErrorDetail | GetClosedatauserbusinessbooleanResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | GetClosedatauserbusinessbooleanResponse200]:
    """EAV boolean-valued user-business field(s) for closed/resolved state (see reference §4)

    Args:
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | GetClosedatauserbusinessbooleanResponse200]
    """

    kwargs = _get_kwargs(
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    origin: str = "https://localhost",
) -> ErrorDetail | GetClosedatauserbusinessbooleanResponse200 | None:
    """EAV boolean-valued user-business field(s) for closed/resolved state (see reference §4)

    Args:
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | GetClosedatauserbusinessbooleanResponse200
    """

    return sync_detailed(
        client=client,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    origin: str = "https://localhost",
) -> Response[ErrorDetail | GetClosedatauserbusinessbooleanResponse200]:
    """EAV boolean-valued user-business field(s) for closed/resolved state (see reference §4)

    Args:
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDetail | GetClosedatauserbusinessbooleanResponse200]
    """

    kwargs = _get_kwargs(
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    origin: str = "https://localhost",
) -> ErrorDetail | GetClosedatauserbusinessbooleanResponse200 | None:
    """EAV boolean-valued user-business field(s) for closed/resolved state (see reference §4)

    Args:
        origin (str):  Default: 'https://localhost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDetail | GetClosedatauserbusinessbooleanResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            origin=origin,
        )
    ).parsed
