import pytest
import numpy as np
from emendo.sensors.generators import AttitudeGenerator, GeneratorConfig

def test_attitude_generator_init_defaults():
    cfg = GeneratorConfig()
    ag = AttitudeGenerator(cfg)
    assert ag.cfg == cfg

def test_attitude_generator_init_none_cfg():
    with pytest.raises(ValueError):
        AttitudeGenerator(None)

def test_attitude_generator_attitude_not_implemented():
    cfg = GeneratorConfig()
    ag = AttitudeGenerator(cfg)
    with pytest.raises(NotImplementedError):
        ag.attitude(0.0, 1.0, 10.0)