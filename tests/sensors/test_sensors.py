import pytest
from emendo.sensors import Sensors, SensorsConfig
from emendo.sensors.generators import GeneratorConfig
from emendo.noises import NoiseConfig
from emendo.sensors.generators import (
    SplineKinematicGenerator,
    GeneratorConfig,
    GeneratorData,
    GeneratorBounds,
    GeneratorZone
)
import numpy as np

# ------------------ Configurations ------------------

# Valid configuration
valid_cfg = SensorsConfig(
    frequency = 100.0,
    generator_cfg = GeneratorConfig(
        max_duration = 6,
        data = GeneratorData(
            timestamps = np.array(range(6)),
            positions = np.ones((6, 3)),
            attitudes = np.ones((6, 3)),
        )
    )
)

# ------------------ Tests: None Config ------------------
def test_missing_config():
    with pytest.raises(ValueError):
        _ = Sensors(None)


# ------------------ Tests: Valid Config ------------------

def test_measurements():
    sensors = Sensors(valid_cfg)
    
    acc, gyro, mag = sensors.measurements()
    
    assert acc.shape[1] == 3
    assert acc.shape[0] == int(sensors.cfg.frequency * sensors.cfg.max_duration)
    
    assert gyro.shape[1] == 3
    assert gyro.shape[0] == int(sensors.cfg.frequency * sensors.cfg.max_duration)
    
    assert mag.shape[1] == 3
    assert mag.shape[0] == int(sensors.cfg.frequency * sensors.cfg.max_duration)
