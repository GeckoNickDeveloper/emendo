import pytest
import numpy as np
from datetime import datetime
from emendo.sensors.generators import GeneratorZone, GeneratorBounds, GeneratorData, GeneratorConfig

# ---------- GeneratorZone Tests ----------

def test_generator_zone_defaults():
    zone = GeneratorZone()
    assert zone.x == (-5000.0, 5000.0)
    assert zone.y == (-5000.0, 5000.0)
    assert zone.z == (0.0, 10000.0)

@pytest.mark.parametrize("axis,name,min_val,max_val", [
    ((-6000, 0), "x", -5000, 5000),
    ((0, 6000), "y", -5000, 5000),
    ((-1, 0), "z", 0, 10000),
])
def test_generator_zone_out_of_bounds(axis, name, min_val, max_val):
    kwargs = dict(x=(0,0), y=(0,0), z=(0,0))
    kwargs[name] = axis
    with pytest.raises(ValueError):
        GeneratorZone(**kwargs)

def test_generator_zone_invalid_length():
    with pytest.raises(ValueError):
        GeneratorZone(x=(0.0,))

def test_generator_zone_none_axis():
    with pytest.raises(ValueError):
        GeneratorZone(x=None)

# ---------- GeneratorBounds Tests ----------

def test_generator_bounds_defaults():
    bounds = GeneratorBounds()
    assert bounds.max_acceleration == 500.0
    assert bounds.max_velocity == 3300.0
    assert isinstance(bounds.zone, GeneratorZone)

@pytest.mark.parametrize("name,value,min_val,max_val", [
    ("max_acceleration", -1, 0, 500),
    ("max_acceleration", 501, 0, 500),
    ("max_velocity", -1, 0, 3300),
    ("max_velocity", 3301, 0, 3300),
])
def test_generator_bounds_invalid_params(name, value, min_val, max_val):
    kwargs = dict(max_acceleration=500, max_velocity=3300)
    kwargs[name] = value
    with pytest.raises(ValueError):
        GeneratorBounds(**kwargs)

def test_generator_bounds_none_zone():
    with pytest.raises(ValueError):
        GeneratorBounds(zone=None)

# ---------- GeneratorData Tests ----------

def test_generator_data_defaults():
    data = GeneratorData()
    assert data.anchor == (0.0,0.0,0.0)
    assert data.timestamps.size == 0
    assert data.positions.shape == (0,3)
    assert data.attitudes.shape == (0,3)
    assert isinstance(data.date, datetime)

def test_generator_data_invalid_anchor_length():
    with pytest.raises(ValueError):
        GeneratorData(anchor=(0.0,0.0))

def test_generator_data_invalid_anchor_range():
    with pytest.raises(ValueError):
        GeneratorData(anchor=(100.0,0.0,0.0))  # lat out of range
    with pytest.raises(ValueError):
        GeneratorData(anchor=(0.0,200.0,0.0))  # lon out of range
    with pytest.raises(ValueError):
        GeneratorData(anchor=(0.0,0.0,60000.0))  # alt out of range

def test_generator_data_invalid_shapes():
    ts = np.array([0,1])
    pos = np.empty((1,3))
    att = np.empty((2,3))
    with pytest.raises(ValueError):
        GeneratorData(timestamps=ts, positions=pos, attitudes=att)

def test_generator_data_invalid_dimensions():
    with pytest.raises(ValueError):
        GeneratorData(timestamps=np.array([[0,1]]))
    with pytest.raises(ValueError):
        GeneratorData(positions=np.empty((2,2)))
    with pytest.raises(ValueError):
        GeneratorData(attitudes=np.empty((2,2)))

# ---------- GeneratorConfig Tests ----------

def test_generator_config_defaults():
    cfg = GeneratorConfig()
    assert isinstance(cfg.bounds, GeneratorBounds)
    assert isinstance(cfg.data, GeneratorData)
    assert cfg.max_duration == 600.0
    assert cfg.kinematic in ['default','spline']
    assert cfg.attitude in ['default','spline']
    assert cfg.magnetic in ['default','regular-grid']

def test_generator_config_invalid_max_duration():
    with pytest.raises(ValueError):
        GeneratorConfig(max_duration=0)

@pytest.mark.parametrize("attr,value,options", [
    ("kinematic", "invalid", ['default','spline']),
    ("attitude", "invalid", ['default','spline']),
    ("magnetic", "invalid", ['default','regular-grid']),
])
def test_generator_config_invalid_options(attr, value, options):
    kwargs = dict()
    kwargs[attr] = value
    with pytest.raises(ValueError):
        GeneratorConfig(**kwargs)