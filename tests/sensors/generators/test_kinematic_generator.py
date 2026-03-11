import pytest
from emendo.sensors.generators import KinematicGenerator, GeneratorConfig

def test_kinematic_generator_init_defaults():
    cfg = GeneratorConfig()
    kg = KinematicGenerator(cfg)
    assert kg.cfg == cfg

def test_kinematic_generator_init_none_cfg():
    with pytest.raises(ValueError):
        KinematicGenerator(None)

@pytest.mark.parametrize("method_name", ["position", "velocity", "acceleration"])
def test_kinematic_generator_methods_not_implemented(method_name):
    cfg = GeneratorConfig()
    kg = KinematicGenerator(cfg)
    method = getattr(kg, method_name)
    with pytest.raises(NotImplementedError):
        method(0.0, 1.0, 10.0)