# Imports
from . import Noise

from typing import Optional, List
import numpy as np



# Implementation
class CompositeNoise(Noise):
    """Composite of multiple Noise instances"""
    def __init__(
        self,
        noises: List[Noise],
        fs: Optional[float] = None,
        seed: Optional[int] = None
    ):
        self.children = noises if noises is not None else []
        super().__init__(fs=fs, seed=seed)

    def seed(self, seed: int):
        for i, n in enumerate(self.children):
            n.seed(seed + i)

    def frequency(self, fs: float):
        if fs <= 0:
            raise ValueError("fs (sampling frequency) must be positive")
        
        for n in self.children:
            n.frequency(fs)

    def scale(self, scale: float):
        raise NotImplementedError("CompositeNoise does not support a single scale")

    def add(self, noise: Noise):
        """Add a new Noise instance ensuring frequency consistency"""
        if self.fs is not None:
            noise.frequency(self.fs)
        self.children.append(noise)


    def generate(self, samples: int):
        if samples <= 0:
            raise ValueError("`samples` must be positive")
            
        noise = np.zeros(samples)
        
        for n in self.children:
            noise += n.generate(samples)
        
        return noise