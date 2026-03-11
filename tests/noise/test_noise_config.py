# Imports
import emendo as E
import pytest

# Testing
class TestNoiseConfig:
    def test_creation_default(self):
        cfg = E.noises.NoiseConfig()
        assert cfg is not None
    
    def test_creation_parametric(self):
        cfg = E.noises.NoiseConfig(
            'white',
            100.0,
            1.0,
            42
        )
        
        assert cfg is not None
    
    def test_creation_parametric_partial(self):
        cfg = E.noises.NoiseConfig(
            name = 'blue',
            scale = 0.7
        )
        
        assert cfg is not None
        assert cfg.name == 'blue'
        assert cfg.freq == 100.0
        assert cfg.scale == 0.7
        assert cfg.seed == 42
        
    def test_creation_none_seed(self):
        cfg = E.noises.NoiseConfig(
            seed = None
        )
        
        assert cfg is not None
        assert cfg.seed is None
    
    def test_creation_set_none_seed(self):
        cfg = E.noises.NoiseConfig()
        cfg.set_seed(None)
        
        assert cfg.seed is None
        
    def test_negative_frequency(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    freq = -100.0,
                )
    
    def test_zero_frequency(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    freq = 0.0,
                )
    
    def test_none_frequency(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    freq = None,
                )
    
    def test_negative_scale(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    scale = -1.0,
                )
    
    def test_zero_scale(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    scale = 0.0,
                )
    
    def test_none_scale(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseConfig(
                    scale = None,
                )