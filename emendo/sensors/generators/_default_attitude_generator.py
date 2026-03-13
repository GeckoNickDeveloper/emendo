# Imports
from . import GeneratorConfig, AttitudeGenerator
import numpy as np


from scipy.spatial.transform import RotationSpline
from scipy.spatial.transform import Rotation as R

# Implementations
class DefaultAttitudeGenerator(AttitudeGenerator):
    '''
    AttitudeGenerator interface for emendo sensors simulation

    Focused on attitude
    '''
    
    def __init__(self, cfg: GeneratorConfig):
        super().__init__(cfg)
        
        self.__attitude: RotationSpline

        self.__interpolate()
    
    def __interpolate(self):
        times = self.cfg.data.timestamps
        rotations = R.from_euler('xyz', self.cfg.data.attitudes, degrees = True)

        self.__attitude = RotationSpline(times, rotations)
    
    def attitude(self, timesteps: np.ndarray):
        if timesteps is None:
            raise ValueError('`timesteps` cannot be None')
        if timesteps.ndim != 1:
            raise ValueError('`timesteps` must be 1D ndarray with shape (N,)')
        if np.max(timesteps) >= self.cfg.max_duration:
            raise ValueError('`timesteps` must not exceed configuration bounds')
        
        return self.__attitude(timesteps, 0)
    
    def angular_rate(self, timesteps: np.ndarray):
        if timesteps is None:
            raise ValueError('`timesteps` cannot be None')
        if timesteps.ndim != 1:
            raise ValueError('`timesteps` must be 1D ndarray with shape (N,)')
        if np.max(timesteps) >= self.cfg.max_duration:
            raise ValueError('`timesteps` must not exceed configuration bounds')

        return self.__attitude(timesteps, 1)