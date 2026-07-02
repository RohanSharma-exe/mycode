"""
NVIDIA API client.
"""

from __future__ import annotations

from typing import Any

from mycode.runtime.network import HTTPClient
from mycode.runtime.provider_config import ProviderConfig


class NVIDIAClient:
    """Low-level NVIDIA API client."""

    BASE_URL = "https://integrate.api.nvidia.com/v1"

    def __init__(
        self,
        http_client: HTTPClient,
        config: ProviderConfig,
    ) -> None:
        self._http = http_client
        self._config = config

    @property
    def headers(self) -> dict[str, str]:
        """Return HTTP headers."""

        return {
            "Authorization": f"Bearer {self._config.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(
        self,
        messages: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Call NVIDIA Chat Completions."""

        payload = {
            "model": self._config.model,
            "messages": messages,
            "temperature": self._config.temperature,
            "max_tokens": self._config.max_tokens,
            "stream": False,
        }

        response = await self._http.post(
            f"{self.BASE_URL}/chat/completions",
            headers=self.headers,
            json=payload,
        )

        return response.json()
