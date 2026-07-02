"""
NVIDIA API client.
"""

from __future__ import annotations

from typing import Any

from mycode.runtime.models import ChatRequest
from mycode.runtime.network import HTTPClient
from mycode.runtime.provider_config import ProviderConfig


class NVIDIAClient:
    """Low-level NVIDIA API client."""

    def __init__(
        self,
        http_client: HTTPClient,
        config: ProviderConfig,
    ) -> None:
        if not config.api_key:
            raise ValueError("NVIDIA_API_KEY is not configured.")

        if not config.base_url:
            raise ValueError("NVIDIA_BASE_URL is not configured.")

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
        request: ChatRequest,
    ) -> dict[str, Any]:
        """Call the NVIDIA Chat Completions API."""

        payload = {
            "model": request.model or self._config.model,
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in request.messages
            ],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens or self._config.max_tokens,
            "stream": request.stream,
        }

        response = await self._http.post(
            f"{self._config.base_url}/chat/completions",
            headers=self.headers,
            json=payload,
        )

        return response.json()
