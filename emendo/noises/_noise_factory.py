# Imports
from . import (
    NoiseConfig,
    Noise,
    BrownNoise,
    PinkNoise,
    WhiteNoise,
    BlueNoise,
    VioletNoise
)

# Implementations
class NoiseFactory:
    __map = {
        "white": WhiteNoise,
        "brown": BrownNoise,
        "pink": PinkNoise,
        "blue": BlueNoise,
        "violet": VioletNoise,
    }

    @staticmethod
    def create(cfg: NoiseConfig) -> Noise:
        if cfg is None:
            raise ValueError("Configuration can't be None")
        
        cls = NoiseFactory.__map[cfg.name]
        return cls(cfg)