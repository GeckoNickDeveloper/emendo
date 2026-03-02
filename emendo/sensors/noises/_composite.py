# Imports
import numpy as np
from ._noise import Noise

# Implementation
class CompositeNoise(Noise):
    def __init__(self):
        super().__init__(1, 1)
        self.noises = []
    
    
    
    def add(self, noise: Noise):
        self.noises.append(noise)
                    
    
    
    def generate(self, samples: int):
        noise = np.zeros(samples)
        
        for n in self.noises:
            noise += n.generate(samples)
        
        return noise