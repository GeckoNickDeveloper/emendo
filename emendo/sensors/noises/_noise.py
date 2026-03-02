# Imports
import numpy as np
from abc import ABC, abstractmethod

# Implementation
class Noise(ABC):
    def __init__(self, fs: float, seed: int):
        self.frequency(fs)
        self.seed(seed)
    
    def seed(self, seed: int):
        self.rng_generator = np.random.default_rng(seed = seed)
    
    def frequency(self, fs: float):
        if fs <= 0:
            raise ValueError('Sampling Frequency must be positive')
        
        self.fs = fs
        self.dt = 1.0 / fs
    
    @abstractmethod
    def generate(self, samples: int):
        pass
    