# Imports
from dataclasses import dataclass
from typing import Optional

# Implementation
@dataclass(frozen = True)
class NoiseConfig:
    name: str           = 'white-noise'
    freq: float         = 100.0
    scale: float        = 1.0
    seed: Optional[int] = 42

    def __post_init__(self):
        if self.freq <= 0:
            raise ValueError("`freq` must be > 0")
        
        if self.scale <= 0:
            raise ValueError("`scale` must be > 0")
        
    def set_seed(self, seed: int):
        object.__setattr__(self, 'seed', seed)