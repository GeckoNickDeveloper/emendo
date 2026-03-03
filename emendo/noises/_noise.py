# Imports
from typing import Optional
import numpy as np

# Implementation
class Noise:
    """Base class for all noise types"""
    def __init__(
        self,
        fs: Optional[float] = None,
        scale: float = 1.0,
        seed: Optional[int] = None,
    ):
        if fs is not None and fs <= 0:
            raise ValueError("Sampling frequency `fs` must be positive")
        if scale <= 0:
            raise ValueError("`scale` must be positive")

        self.scale = scale
        self.fs = fs
        self.dt = 1.0 / fs if fs else None
        self._rng = np.random.default_rng(seed) if seed is not None else np.random.default_rng()

    def seed(self, seed: int):
        self._rng = np.random.default_rng(seed)

    def frequency(self, fs: float):
        if fs <= 0:
            raise ValueError("Sampling frequency `fs` must be positive")
        self.fs = fs
        self.dt = 1.0 / fs

    def scale(self, scale: float):
        if scale <= 0:
            raise ValueError("`scale` must be positive")
        self.scale = scale

    def generate(self, samples: int):
        raise NotImplementedError("Subclasses must implement generate")
    