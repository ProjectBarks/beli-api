from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_businesses_res_availability_body import CreateBusinessesResAvailabilityBody
from ...models.create_businesses_res_availability_response_200 import CreateBusinessesResAvailabilityResponse200
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: CreateBusinessesResAvailabilityBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/businesses-res-availability/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateBusinessesResAvailabilityResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateBusinessesResAvailabilityResponse200.from_dict(response.json())

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
) -> Response[CreateBusinessesResAvailabilityResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBusinessesResAvailabilityBody,
    origin: str = "https://localhost",
) -> Response[CreateBusinessesResAvailabilityResponse200 | ErrorDetail]:
    """Reservation availability for one or more businesses (response keyed by composite string per
    reference §5/§8 ReservationOffer)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateBusinessesResAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBusinessesResAvailabilityResponse200 | ErrorDetail]
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
    body: CreateBusinessesResAvailabilityBody,
    origin: str = "https://localhost",
) -> CreateBusinessesResAvailabilityResponse200 | ErrorDetail | None:
    """Reservation availability for one or more businesses (response keyed by composite string per
    reference §5/§8 ReservationOffer)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateBusinessesResAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBusinessesResAvailabilityResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBusinessesResAvailabilityBody,
    origin: str = "https://localhost",
) -> Response[CreateBusinessesResAvailabilityResponse200 | ErrorDetail]:
    """Reservation availability for one or more businesses (response keyed by composite string per
    reference §5/§8 ReservationOffer)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateBusinessesResAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBusinessesResAvailabilityResponse200 | ErrorDetail]
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
    body: CreateBusinessesResAvailabilityBody,
    origin: str = "https://localhost",
) -> CreateBusinessesResAvailabilityResponse200 | ErrorDetail | None:
    """Reservation availability for one or more businesses (response keyed by composite string per
    reference §5/§8 ReservationOffer)

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateBusinessesResAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBusinessesResAvailabilityResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
