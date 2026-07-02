"""
Reusable async HTTP client.
"""

from __future__ import annotations

from typing import Any

import httpx

from mycode.runtime.network.exceptions import (
    HTTPRequestError,
    HTTPResponseError,
)


class HTTPClient:
    """Reusable wrapper around httpx.AsyncClient."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        """
        Initialize the HTTP client.

        Args:
            client: Shared AsyncClient instance.
        """
        self._client = client

    async def get(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """Perform a GET request."""

        try:
            response = await self._client.get(
                url,
                headers=headers,
                params=params,
            )

            response.raise_for_status()

            return response

        except httpx.HTTPStatusError as exc:
            raise HTTPResponseError(str(exc)) from exc

        except httpx.HTTPError as exc:
            raise HTTPRequestError(str(exc)) from exc

    async def post(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """Perform a POST request."""

        try:
            response = await self._client.post(
                url,
                headers=headers,
                json=json,
            )

            response.raise_for_status()

            return response

        except httpx.HTTPStatusError as exc:
            raise HTTPResponseError(str(exc)) from exc

        except httpx.HTTPError as exc:
            raise HTTPRequestError(str(exc)) from exc
