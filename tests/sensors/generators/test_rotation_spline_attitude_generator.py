import pytest
import numpy as np
from scipy.spatial.transform import Rotation as R
from emendo.sensors.generators import (
    RotationSplineAttitudeGenerator,
    GeneratorConfig,
    GeneratorData
)

# ------------------ Configurations ------------------

# Valid configuration
valid_cfg = GeneratorConfig(
    data = GeneratorData(
        timestamps = np.array([0, 1, 2, 3, 4, 5]),
        positions = np.ones((6, 3)),
        attitudes = np.ones((6, 3)) * 10.0,  # Euler angles in degrees
    )
)

# ------------------ Tests: Valid Config ------------------

def test_rotation_spline_attitude_generator_attitude_valid():
    ag = RotationSplineAttitudeGenerator(valid_cfg)
    ag._RotationSplineAttitudeGenerator__interpolate()
    ag.attitude(0.0, 1.0, 5.0)  # should run without error

def test_rotation_spline_attitude_generator_angular_rate_valid():
    ag = RotationSplineAttitudeGenerator(valid_cfg)
    ag._RotationSplineAttitudeGenerator__interpolate()
    ag.angular_rate(0.0, 1.0, 5.0)  # should run without error
