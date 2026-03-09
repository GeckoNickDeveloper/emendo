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
        self.cfg = cfg

    def magnetic(self, positions: np.ndarray):
        raise NotImplementedError('Must implement `magnetic` method')