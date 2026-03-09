# Imports
from . import GeneratorConfig

import numpy as np

# Implementations
class GeneratorProxy():
    '''
    Generator API for emendo sensor simulation
    '''

    def __init__(self, config: GeneratorConfig):
        self.config = config
        
        # Selector for KinematicGenerator
        # self.kinematic
        # Selector for AttitudeGenerator
        # self.attitude
        # Selector for MagneticGenerator
        # self.magnetic
    

    
    def position(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `position` method')
    
    def velocity(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `velocity` method')
    
    def acceleration(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `acceleration` method')
    
    def attitude(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `attitude` method')
    
    def magnetic(self, position: np.ndarray):
        raise NotImplementedError('Subclasses must implement `magnetic` method')