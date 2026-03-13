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
            raise ValueError('`cfg` cannot be None')
        if not isinstance(cfg, GeneratorConfig):
            raise ValueError('`cfg` must be a `GeneratorConfig`')
        
        self.cfg = cfg

    def position(self, timesteps: np.ndarray):
        raise NotImplementedError('Must implement `position` method')
    
    def velocity(self, timesteps: np.ndarray):
        raise NotImplementedError('Must implement `velocity` method')
    
    def acceleration(self, timesteps: np.ndarray):
        raise NotImplementedError('Must implement `acceleration` method')