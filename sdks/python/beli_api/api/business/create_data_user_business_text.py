from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_data_user_business_text_body import CreateDataUserBusinessTextBody
from ...models.create_data_user_business_text_response_200 import CreateDataUserBusinessTextResponse200
from ...models.error_detail import ErrorDetail
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDataUserBusinessTextBody,
    origin: str = "https://localhost",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Origin"] = origin

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/data-user-business-text-new/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDataUserBusinessTextResponse200 | ErrorDetail | None:
    if response.status_code == 200:
        response_200 = CreateDataUserBusinessTextResponse200.from_dict(response.json())

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
) -> Response[CreateDataUserBusinessTextResponse200 | ErrorDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataUserBusinessTextBody,
    origin: str = "https://localhost",
) -> Response[CreateDataUserBusinessTextResponse200 | ErrorDetail]:
    """Write user-business text (e.g. NOTES/review text) via the EAV layer

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateDataUserBusinessTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDataUserBusinessTextResponse200 | ErrorDetail]
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
    body: CreateDataUserBusinessTextBody,
    origin: str = "https://localhost",
) -> CreateDataUserBusinessTextResponse200 | ErrorDetail | None:
    """Write user-business text (e.g. NOTES/review text) via the EAV layer

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateDataUserBusinessTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDataUserBusinessTextResponse200 | ErrorDetail
    """

    return sync_detailed(
        client=client,
        body=body,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataUserBusinessTextBody,
    origin: str = "https://localhost",
) -> Response[CreateDataUserBusinessTextResponse200 | ErrorDetail]:
    """Write user-business text (e.g. NOTES/review text) via the EAV layer

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateDataUserBusinessTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDataUserBusinessTextResponse200 | ErrorDetail]
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
    body: CreateDataUserBusinessTextBody,
    origin: str = "https://localhost",
) -> CreateDataUserBusinessTextResponse200 | ErrorDetail | None:
    """Write user-business text (e.g. NOTES/review text) via the EAV layer

    Args:
        origin (str):  Default: 'https://localhost'.
        body (CreateDataUserBusinessTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDataUserBusinessTextResponse200 | ErrorDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            origin=origin,
        )
    ).parsed
