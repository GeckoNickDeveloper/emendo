# Imports
from . import NoiseConfig
from typing import Tuple
import numpy as np

# Implementation
class Noise:
    def __init__(self, cfg: NoiseConfig):
        if cfg is None:
            raise ValueError("`cfg` cannot be None")
        
        self.cfg = cfg
        self.rng = np.random.default_rng(cfg.seed)

    def seed(self, seed: int) -> None:
        self.cfg.set_seed(seed)
        self.rng = np.random.default_rng(self.cfg.seed)

    def generate(self, shape: Tuple[int, int], frequency: float) -> np.ndarray:
        raise NotImplementedError("`generate` must implement generate")