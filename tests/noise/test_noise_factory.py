# Imports
import emendo as E
import pytest

# Testing
class TestNoiseFactory:
    def test_white_noise_creation(self):
        cfg = E.noises.NoiseConfig(
            name    = "white",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        noise = E.noises.NoiseFactory.create(cfg)
        
        assert isinstance(noise, E.noises.WhiteNoise)
    
    def test_brown_noise_creation(self):
        cfg = E.noises.NoiseConfig(
            name    = "brown",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        noise = E.noises.NoiseFactory.create(cfg)
        
        assert isinstance(noise, E.noises.BrownNoise)
    
    def test_pink_noise_creation(self):
        cfg = E.noises.NoiseConfig(
            name    = "pink",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        noise = E.noises.NoiseFactory.create(cfg)
        
        assert isinstance(noise, E.noises.PinkNoise)
    
    def test_blue_noise_creation(self):
        cfg = E.noises.NoiseConfig(
            name    = "blue",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        noise = E.noises.NoiseFactory.create(cfg)
        
        assert isinstance(noise, E.noises.BlueNoise)
    
    def test_violet_noise_creation(self):
        cfg = E.noises.NoiseConfig(
            name    = "violet",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        noise = E.noises.NoiseFactory.create(cfg)
        
        assert isinstance(noise, E.noises.VioletNoise)
        
    def test_wrong_noise_name(self):
        cfg = E.noises.NoiseConfig(
            name    = "green",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )
        
        with pytest.raises(KeyError):
            _ = E.noises.NoiseFactory.create(cfg)
            
    def test_none_config(self):
        with pytest.raises(ValueError):
            _ = E.noises.NoiseFactory.create(None)