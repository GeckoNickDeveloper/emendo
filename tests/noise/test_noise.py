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

    def test_raise_not_implemented(self, config):
        noise = E.noises.Noise(config)
        
        with pytest.raises(NotImplementedError):
            noise.generate(1000)
    