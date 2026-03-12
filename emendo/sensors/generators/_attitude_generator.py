# Imports
from . import GeneratorConfig
import numpy as np

# Implementations
class AttitudeGenerator:
    '''
    AttitudeGenerator interface for emendo sensors simulation

    Focused on attitude
    '''
    
    def __init__(self, cfg: GeneratorConfig):
        if cfg is None:
            raise ValueError('`GeneratorConfig` cannot be `None`')
        
        self.cfg = cfg
    
    def attitude(self, timesteps: np.ndarray):
        raise NotImplementedError('Must implement `attitude` method')
    
    def angular_rate(self, timesteps: np.ndarray):
        raise NotImplementedError('Must implement `attitude` method')