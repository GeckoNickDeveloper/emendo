# Imports
import emendo as E
import pytest

# Testing
class TestNoise:
    
    @pytest.fixture
    def config(self):
        return E.noises.NoiseConfig(
            name    = "white",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            _ = E.noises.Noise(None)
    
    def test_init(self, config):
        noise = E.noises.Noise(config)
        
        assert noise is not None

    def test_seed(self, config):
        noise = E.noises.Noise(config)
        noise.seed(34)
        
        assert noise.cfg.seed == 34

    def test_raise_not_implemented(self, config):
        noise = E.noises.Noise(config)
        
        with pytest.raises(NotImplementedError):
            noise.generate(1000)
    