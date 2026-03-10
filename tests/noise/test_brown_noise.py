# Imports
import emendo as E
import numpy as np
import pytest

# Testing
class TestBrownNoise:
    @pytest.fixture
    def config(self):
        return E.noises.NoiseConfig(
            name    = "brown",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )

    def test_generate_shape(self, config):
        n = 1_000
        noise = E.noises.BrownNoise(config)
        samples = noise.generate(n)

        assert isinstance(samples, np.ndarray)
        assert samples.shape == (n,)

    def test_reproducibility_same_configs(self, config):
        n = 1_000
        noise1 = E.noises.BrownNoise(config)
        noise2 = E.noises.BrownNoise(config)

        s1 = noise1.generate(n)
        s2 = noise2.generate(n)

        assert np.array_equal(s1, s2)
    
    def test_reproducibility_seed_reset(self, config):
        n = 1_000
        noise = E.noises.BrownNoise(config)
        base_seed = noise.cfg.seed
        
        s1 = noise.generate(n)
        noise.seed(base_seed)
        s2 = noise.generate(n)

        assert np.array_equal(s1, s2)

    def test_scale_effect(self):
        cfg_small = E.noises.NoiseConfig(
            name = "brown",
            freq = 100.0,
            scale = 0.5,
            seed = 1
        )
        cfg_big = E.noises.NoiseConfig(
            name = "brown",
            freq = 100.0,
            scale = 2.0,
            seed = 1
        )

        n = 1_000
        s1 = E.noises.BrownNoise(cfg_small).generate(n)
        s2 = E.noises.BrownNoise(cfg_big).generate(n)

        assert np.std(s2) > np.std(s1)