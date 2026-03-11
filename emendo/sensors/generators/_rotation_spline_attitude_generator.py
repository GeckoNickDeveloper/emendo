# Imports
from . import GeneratorConfig, AttitudeGenerator
import numpy as np


from scipy.spatial.transform import RotationSpline

# Implementations
class RotationSplineAttitudeGenerator(AttitudeGenerator):
    '''
    AttitudeGenerator interface for emendo sensors simulation

    Focused on attitude
    '''
    
    def __init__(self, cfg: GeneratorConfig):
        super().__init__(cfg)
        
        self.__attitude: RotationSpline
    
    def __interpolate(self):
        #self.__trajectory = sp.interpolate.make_interp_spline(
        #    self.cfg.data.timestamps,
        #    self.cfg.data.attitudes,
        #    k = 3,
        #    bc_type = bc
        #)
        pass
    
    def attitude(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Must implement `attitude` method')