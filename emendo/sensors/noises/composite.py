# Imports
import numpy as np
from .noise import Noise

# Implementation
class CompositeNoise(Noise):
    def __init__(self, noises: list[Noise] = []):
        self.noises = noises
        
    def add(self, noise: Noise):
        self.noises.append(noise)
    
    def generate(self, N: int):
        noise = np.zeros(N)
        
        for n in self.noises:
            noise += n.generate(N)
        
        return noise