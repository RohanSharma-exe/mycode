from mycode.runtime import ProviderConfig


def test_provider_config_defaults() -> None:
    config = ProviderConfig(
        name="nvidia",
        model="test-model",
    )

    assert config.timeout == 120.0

    assert config.temperature == 0.7

    assert config.max_tokens == 4096

    assert config.enable_streaming
