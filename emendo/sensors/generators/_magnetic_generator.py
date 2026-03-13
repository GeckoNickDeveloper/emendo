# Imports
from . import GeneratorConfig
import numpy as np



# Implementations
class MagneticGenerator:
    '''
    MagneticGenerator interface for emendo sensors simulation

    Focused on magnetic field
    '''
    
    def __init__(self, cfg: GeneratorConfig):
        if cfg is None:
            raise ValueError('`cfg` cannot be None')
        if not isinstance(cfg, GeneratorConfig):
            raise ValueError('`cfg` must be a `GeneratorConfig`')
        
        self.cfg = cfg

    def magnetic(self, positions: np.ndarray):
        raise NotImplementedError('Must implement `magnetic` method')