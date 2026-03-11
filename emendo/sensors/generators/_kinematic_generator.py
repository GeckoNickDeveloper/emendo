# Imports
from . import GeneratorConfig
import numpy as np

# Implementations
class KinematicGenerator:
    '''
    `KinematicGenerator` interface for emendo sensors simulation
    
    Focused on trajectory, velocity and acceleration
    '''
    def __init__(self, cfg: GeneratorConfig):
        if cfg is None:
            raise ValueError('`GeneratorConfig` cannot be `None`')
        
        self.cfg = cfg

    def position(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Must implement `position` method')
    
    def velocity(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Must implement `velocity` method')
    
    def acceleration(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Must implement `acceleration` method')