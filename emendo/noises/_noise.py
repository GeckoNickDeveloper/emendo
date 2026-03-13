# Imports
from . import NoiseConfig
from typing import Tuple
import numpy as np

# Implementation
class Noise:
    def __init__(self, cfg: NoiseConfig):
        if cfg is None:
            raise ValueError("Configuration can't be None")
        
        self.cfg = cfg
        self.rng = np.random.default_rng(cfg.seed)

    def seed(self, seed: int):
        self.cfg.set_seed(seed)
        self.rng = np.random.default_rng(self.cfg.seed)

    def generate(self, shape: Tuple[int, int], frequency: float):
        raise NotImplementedError("`generate` must implement generate")