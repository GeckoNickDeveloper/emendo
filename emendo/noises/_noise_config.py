# Imports
from dataclasses import dataclass
from typing import Optional

# Implementation
@dataclass(frozen = True)
class NoiseConfig:
    name: str           = 'white'
    scale: float        = 1.0
    seed: Optional[int] = 42

    def __post_init__(self) -> None:        
        if self.scale is None or self.scale <= 0:
            raise ValueError("`scale` must be > 0")
        
    def set_seed(self, seed: Optional[int]) -> None:
        object.__setattr__(self, 'seed', seed)