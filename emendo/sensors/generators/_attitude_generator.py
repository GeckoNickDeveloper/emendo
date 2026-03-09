# Imports
from . import GeneratorConfig
import numpy as np

from scipy.spatial.transform import RotationSpline

# Implementations
class AttitudeGenerator:
    '''
    AttitudeGenerator interface for emendo sensors simulation

    Focused on attitude
    '''
    
    def __init__(self, cfg: GeneratorConfig):
        self.cfg = cfg
    
    def attitude(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Must implement `attitude` method')