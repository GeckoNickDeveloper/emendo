# Imports
from .generators import GeneratorProxy
from ..noises import BaseNoise

# Implementation
class Sensors():
    def __init__(self, generator: GeneratorProxy, noise: BaseNoise, freq: float, duration: float, aliasing: bool = True):
        self.generator = generator
        self.noise = noise
        self.freq = freq
        self.duration = duration
        self.aliasing = aliasing
    
    # Obtain measurements data
    def measurements(self):
        # Get true accelerometer (10x oversample)
        # Get true orientation (10x oversample)
        # Get true magnetometer (10x oversample)
        
        # Get noise modeling (10x oversample)
        
        # Rotate to body frame
        # Add noise
        
        # Anti-aliasing filter (optional)
        
        # Downsample (decimation)
        pass