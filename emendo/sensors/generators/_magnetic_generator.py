# Imports
from . import GeneratorConfig
from . import BaseGenerator

from scipy.interpolate import RBFInterpolator

import numpy as np



# Implementations
class MagneticGenerator(BaseGenerator):
    '''
    MagneticGenerator interface for emendo sensors simulation

    Focused on magnetic field interpolation
    '''
    def __init__(self, config: GeneratorConfig):
        super().__init__(config)
        
        # Interpolate megnatic field
    


    def magnetic(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `magnetic` method')