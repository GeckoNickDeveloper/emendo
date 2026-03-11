# Imports
from . import GeneratorConfig, AttitudeGenerator
import numpy as np


from scipy.spatial.transform import RotationSpline
from scipy.spatial.transform import Rotation as R

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
        times = self.cfg.data.timestamps
        rotations = R.from_euler('xyz', self.cfg.data.attitudes, degrees = True)

        self.__attitude = RotationSpline(times, rotations)
    
    def attitude(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration + 0.5 * dt, dt)

        self.__attitude(t, 0)
    
    def angular_rate(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration + 0.5 * dt, dt)

        self.__attitude(t, 1)