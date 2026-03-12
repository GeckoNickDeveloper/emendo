# Imports
from dataclasses import dataclass, field
from .generators import GeneratorConfig
from ..noises import NoiseConfig

# Implementations
@dataclass(frozen = True)
class SensorsConfig:
    generator_cfg: GeneratorConfig = field(default_factory = GeneratorConfig)
    noise_cfg: NoiseConfig         = field(default_factory = NoiseConfig)
    max_duration: float            = 600.0
    frequency: float               = 100.0
    aliasing: bool                 = False

    def __post_init__(self):
        if self.generator_cfg is None:
            raise ValueError("`generator_cfg` cannot be None")
        if self.noise_cfg is None:
            raise ValueError("`noise_cfg` cannot be None")

        if self.max_duration is None or self.max_duration <= 0.0:
            raise ValueError("`max_duration` must be > 0")
        if self.frequency is None or self.frequency <= 0.0:
            raise ValueError("`frequency` must be > 0")

        if not isinstance(self.aliasing, bool):
            raise TypeError("`aliasing` must be a boolean")