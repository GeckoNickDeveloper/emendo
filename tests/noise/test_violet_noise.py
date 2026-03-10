# Imports
import emendo as E
import numpy as np
import pytest

# Testing
class TestVioletNoise:
    @pytest.fixture
    def config(self):
        return E.noises.NoiseConfig(
            name    = "violet",
            freq    = 100.0,
            scale   = 1.0,
            seed    = 42
        )

    def test_init(self, config):
        noise = E.noises.VioletNoise(config)
        assert noise is not None

    def test_generate_shape(self, config):
        noise = E.noises.VioletNoise(config)
        n = 1000
        samples = noise.generate(n)

        assert isinstance(samples, np.ndarray)
        assert samples.shape == (n,)

    def test_reproducibility(self, config):
        n = 500

        noise1 = E.noises.VioletNoise(config)
        noise2 = E.noises.VioletNoise(config)

        s1 = noise1.generate(n)
        s2 = noise2.generate(n)

        assert np.array_equal(s1, s2)

    def test_scale_effect(self):
        cfg_small = E.noises.NoiseConfig(
            name = "violet",
            freq = 100.0,
            scale = 0.5,
            seed = 1
        )
        cfg_big = E.noises.NoiseConfig(
            name = "violet",
            freq = 100.0,
            scale = 2.0,
            seed = 1
        )

        n = 10000
        s1 = E.noises.VioletNoise(cfg_small).generate(n)
        s2 = E.noises.VioletNoise(cfg_big).generate(n)

        assert np.std(s2) > np.std(s1)