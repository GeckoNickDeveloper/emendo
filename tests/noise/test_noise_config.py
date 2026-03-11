import pytest
import emendo as E


# --- NoiseConfig Creation Tests ---

def test_noiseconfig_default_creation():
    cfg = E.noises.NoiseConfig()
    assert cfg is not None


def test_noiseconfig_parametric_creation():
    cfg = E.noises.NoiseConfig('white', 100.0, 1.0, 42)
    assert cfg is not None


def test_noiseconfig_partial_creation():
    cfg = E.noises.NoiseConfig(name='blue', scale=0.7)
    assert cfg is not None
    assert cfg.name == 'blue'
    assert cfg.freq == 100.0
    assert cfg.scale == 0.7
    assert cfg.seed == 42


def test_noiseconfig_none_seed():
    cfg = E.noises.NoiseConfig(seed=None)
    assert cfg is not None
    assert cfg.seed is None


def test_noiseconfig_set_seed_none():
    cfg = E.noises.NoiseConfig()
    cfg.set_seed(None)
    assert cfg.seed is None


# --- NoiseConfig Parameter Validation ---

@pytest.mark.parametrize("freq", [None, 0.0, -100.0])
def test_noiseconfig_invalid_frequency(freq):
    with pytest.raises(ValueError):
        E.noises.NoiseConfig(freq=freq)


@pytest.mark.parametrize("scale", [None, 0.0, -1.0])
def test_noiseconfig_invalid_scale(scale):
    with pytest.raises(ValueError):
        E.noises.NoiseConfig(scale=scale)