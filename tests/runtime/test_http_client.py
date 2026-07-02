import httpx

from mycode.runtime.network import HTTPClient


def test_create_http_client() -> None:
    async_client = httpx.AsyncClient()

    client = HTTPClient(async_client)

    assert client is not None

    assert client._client is async_client

    # Close immediately to avoid resource warnings.
    import asyncio

    asyncio.run(async_client.aclose())
