# Imports
from . import NoiseConfig
from typing import Tuple, Optional
import numpy as np

# Implementation
class Noise:
    def __init__(self, cfg: NoiseConfig):
        if cfg is None:
            raise ValueError('`cfg` cannot be None')
        
        self.cfg = cfg
        self.rng = np.random.default_rng(cfg.seed)

    def seed(self, seed: Optional[int]) -> None:
        if seed is not None and not isinstance(seed, int):
            raise TypeError('`seed` must be None or an integer')

        self.cfg.set_seed(seed)
        self.rng = np.random.default_rng(self.cfg.seed)

    def generate(self, shape: Tuple[int, int], frequency: float) -> np.ndarray:
        raise NotImplementedError('`generate` must implement generate')