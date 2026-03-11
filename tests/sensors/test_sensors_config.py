import pytest
from emendo.sensors import SensorsConfig
from emendo.sensors.generators import GeneratorConfig
from emendo.noises import NoiseConfig


# --- Valid instantiation tests ---

def test_default_instantiation():
    cfg = SensorsConfig()
    assert isinstance(cfg.generator_cfg, GeneratorConfig)
    assert isinstance(cfg.noise_cfg, NoiseConfig)
    assert cfg.max_duration == 600.0
    assert cfg.frequency == 100.0
    assert cfg.aliasing is False


def test_custom_values():
    gen_cfg = GeneratorConfig(max_duration=1200.0)
    noise_cfg = NoiseConfig(freq=200.0, scale=2.0)
    cfg = SensorsConfig(
        generator_cfg=gen_cfg,
        noise_cfg=noise_cfg,
        max_duration=300.0,
        frequency=50.0,
        aliasing=True
    )
    assert cfg.generator_cfg.max_duration == 1200.0
    assert cfg.noise_cfg.freq == 200.0
    assert cfg.max_duration == 300.0
    assert cfg.frequency == 50.0
    assert cfg.aliasing is True


# --- Invalid generator_cfg ---

def test_none_generator_cfg():
    with pytest.raises(ValueError):
        SensorsConfig(generator_cfg=None)


# --- Invalid noise_cfg ---

def test_none_noise_cfg():
    with pytest.raises(ValueError):
        SensorsConfig(noise_cfg=None)


# --- Invalid max_duration ---

@pytest.mark.parametrize("value", [0, -10, None])
def test_invalid_max_duration(value):
    with pytest.raises(ValueError):
        SensorsConfig(max_duration=value)


# --- Invalid frequency ---

@pytest.mark.parametrize("value", [0, -5, None])
def test_invalid_frequency(value):
    with pytest.raises(ValueError):
        SensorsConfig(frequency=value)


# --- Invalid aliasing type ---

@pytest.mark.parametrize("value", [None, 1, "False"])
def test_invalid_aliasing(value):
    with pytest.raises(TypeError):
        SensorsConfig(aliasing=value)