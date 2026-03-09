# Imports
from . import NoiseConfig
import numpy as np

# Implementation
class Noise:
    def __init__(self, cfg: NoiseConfig):
        self.cfg = cfg
        self.rng = np.random.default_rng(cfg.seed)

    def generate(self, N: int):
        raise NotImplementedError("Subclasses must implement generate")
    