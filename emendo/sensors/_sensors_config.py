# Imports
from dataclasses import dataclass
from .generators import GeneratorConfig
from ..noises import NoiseConfig

# Implementations
@dataclass(frozen = True)
class SensorsConfig:
    generator: GeneratorConfig
    noise: NoiseConfig
    max_duration: float         = 600.0
    frequency: float            = 100.0
    aliasing: bool              = False
    
    def __post_init__(self):
        if self.max_duration <= 0.0:
            raise ValueError("`max_duration` must be > 0")
        
        if self.frequency <= 0.0:
            raise ValueError("`frequency` value must be > 0")