# Imports
from dataclasses import dataclass, field
from .generators import GeneratorConfig
from ..noises import NoiseConfig

# Implementations
@dataclass(frozen = True)
class SensorsConfig:
    generator_cfg: GeneratorConfig  = field(default_factory = GeneratorConfig)
    acc_noise_cfg: NoiseConfig      = field(default_factory = NoiseConfig)
    gyro_noise_cfg: NoiseConfig     = field(default_factory = NoiseConfig)
    mag_noise_cfg: NoiseConfig      = field(default_factory = NoiseConfig)
    max_duration: float             = 600.0
    frequency: float                = 100.0
    aliasing: bool                  = False

    def __post_init__(self) -> None:
        # Generator Config
        if self.generator_cfg is None:
            raise ValueError('`generator_cfg` cannot be None')
        if not isinstance(self.generator_cfg, GeneratorConfig):
            raise ValueError('`generator_cfg` must be a `GeneratorConfig`')
            
        

        # Noise Configs
        ## Accelerometer
        if self.acc_noise_cfg is None:
            raise ValueError('`acc_noise_cfg` cannot be None')
        if not isinstance(self.acc_noise_cfg, NoiseConfig):
            raise ValueError('`acc_noise_cfg` must be a `NoiseConfig`')
        ## Gyroscope
        if self.gyro_noise_cfg is None:
            raise ValueError('`gyro_noise_cfg` cannot be None')
        if not isinstance(self.gyro_noise_cfg, NoiseConfig):
            raise ValueError('`gyro_noise_cfg` must be a `NoiseConfig`')
        ## Magnetometer
        if self.mag_noise_cfg is None:
            raise ValueError('`mag_noise_cfg` cannot be None')
        if not isinstance(self.mag_noise_cfg, NoiseConfig):
            raise ValueError('`mag_noise_cfg` must be a `NoiseConfig`')



        # General Config
        if self.max_duration is None or self.max_duration <= 0.0:
            raise ValueError('`max_duration` must be > 0')
        if self.frequency is None or self.frequency <= 0.0:
            raise ValueError('`frequency` must be > 0')
        if not isinstance(self.aliasing, bool):
            raise TypeError('`aliasing` must be a boolean')