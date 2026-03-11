import pytest
import numpy as np
from emendo.sensors.generators import (
    SplineKinematicGenerator,
    GeneratorConfig,
    GeneratorData,
    GeneratorBounds,
    GeneratorZone
)

# ------------------ Configurations ------------------

# Valid configuration
valid_cfg = GeneratorConfig(
    max_duration = 6,
    data = GeneratorData(
        timestamps = np.array(range(6)),
        positions = np.ones((6, 3)),
        attitudes = np.ones((6, 3)),
    )
)

# Invalid: positions exceed zone bounds (+-5000)
invalid_cfg_positions_exceed = GeneratorConfig(
    max_duration = 6,
    data = GeneratorData(
        timestamps = np.array(range(6)),
        positions = np.array([
            [6000, 0, 0],
            [0, 6000, 0],
            [0, 0, 11000],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]),
        attitudes = np.ones((6,3)),
    )
)

# ------------------ Tests: Valid Config ------------------

def test_spline_kinematic_position_valid():
    kg = SplineKinematicGenerator(valid_cfg)
    pos = kg.position(0.0, 1.0, 5.0)
    assert pos.shape[1] == 3
    assert pos.shape[0] > 0

def test_spline_kinematic_velocity_valid():
    kg = SplineKinematicGenerator(valid_cfg)
    vel = kg.velocity(0.0, 1.0, 5.0)
    assert vel.shape[1] == 3
    assert vel.shape[0] > 0

def test_spline_kinematic_acceleration_valid():
    kg = SplineKinematicGenerator(valid_cfg)
    acc = kg.acceleration(0.0, 1.0, 5.0)
    assert acc.shape[1] == 3
    assert acc.shape[0] > 0

def test_spline_kinematic_lengths_consistency_valid():
    kg = SplineKinematicGenerator(valid_cfg)
    pos = kg.position(0.0, 1.0, 5.0)
    vel = kg.velocity(0.0, 1.0, 5.0)
    acc = kg.acceleration(0.0, 1.0, 5.0)
    assert pos.shape[0] == vel.shape[0] == acc.shape[0]

# ------------------ Tests: Invalid Config ------------------

def test_spline_kinematic_invalid_positions_exceed_bounds():
    with pytest.raises(ValueError):
        SplineKinematicGenerator(invalid_cfg_positions_exceed)