import pytest
import numpy as np
from emendo.sensors.generators import MagneticGenerator, GeneratorConfig

def test_magnetic_generator_init_defaults():
    cfg = GeneratorConfig()
    mg = MagneticGenerator(cfg)
    assert mg.cfg == cfg

def test_magnetic_generator_init_none_cfg():
    with pytest.raises(ValueError):
        MagneticGenerator(None)

def test_magnetic_generator_magnetic_not_implemented():
    cfg = GeneratorConfig()
    mg = MagneticGenerator(cfg)
    positions = np.empty((0,3))
    with pytest.raises(NotImplementedError):
        mg.magnetic(positions)