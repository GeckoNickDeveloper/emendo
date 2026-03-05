# Imports
from . import GeneratorConfig
from . import BaseGenerator

from scipy.spatial.transform import RotationSpline

import numpy as np



# Implementations
class AttitudeGenerator(BaseGenerator):
    '''
    AttitudeGenerator interface for emendo sensors simulation

    Focused on attitude interpolation
    '''
    def __init__(self, config: GeneratorConfig):
        super().__init__(config)
        
        # Interpolate attitude
    


    def attitude(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `attitude` method')