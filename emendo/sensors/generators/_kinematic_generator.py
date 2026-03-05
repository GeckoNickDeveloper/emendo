# Imports
from . import GeneratorConfig
from . import BaseGenerator

from scipy.interpolate import BSpline
from scipy.spatial.transform import RotationSpline
from scipy.interpolate import RBFInterpolator

import numpy as np



# Implementations
class KinematicGenerator(BaseGenerator):
    '''
    SplineGenerator for emendo sensors simulation

    Based on splines
    '''
    def __init__(self, config: GeneratorConfig):
        super().__init__(config)
        
        # Create trajectory interpolations
        # Find min/max
        # Raise error out-of-bounds if hard boundaries reached
    
    def limits(self):
        '''
        Returns the kinematic zone limits
        '''
        raise NotImplementedError('Subclasses must implement `limits` method')

    def position(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `position` method')
    
    def velocity(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `velocity` method')
    
    def acceleration(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `acceleration` method')