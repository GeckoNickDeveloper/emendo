'''
TODO:
    - Improve code
'''
# Imports
from . import GeneratorConfig, KinematicGenerator
import scipy as sp
import numpy as np

# Implementations
class SplineKinematicGenerator(KinematicGenerator):
    '''
    SplineKinematicGenerator for emendo sensors simulation

    Based on splines
    '''
    def __init__(self, cfg: GeneratorConfig):
        super().__init__(cfg)
        
        # Attributes
        self.__trajectory: sp.interpolate.BSpline
        self.__velocity: sp.interpolate.BSpline
        self.__acceleration: sp.interpolate.BSpline
                
        # Initialization
        self.__interpolate()
        self.__validate()
    
    
    
    def __interpolate(self):
        bc = ([(2, np.zeros(3))], [(2, np.zeros(3))])
        self.__trajectory = sp.interpolate.make_interp_spline(
            self.cfg.data.timestamps,
            self.cfg.data.positions,
            k = 3,
            bc_type = bc
        )
        
        self.__velocity = self.__trajectory.derivative(1)
        self.__acceleration = self.__trajectory.derivative(2)
    
    def __validate(self):
        # Optimize Splines & Boundary checking
        ## Position
        pos_x_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[0],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        pos_x_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[0],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        pos_y_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[1],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        pos_y_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[1],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        pos_z_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[2],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        pos_z_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[2],
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        
        ### Check successes
        if not (
            pos_x_min.success and pos_x_max.success and
            pos_y_min.success and pos_y_max.success and
            pos_z_min.success and pos_z_max.success
        ):
            # TODO Improve
            raise ValueError('OptimizeException for position')
        
        ### Check bounds
        if not (
            ((pos_x_min.fun >= self.cfg.bounds.zone.x[0]) and (pos_x_max.fun <= self.cfg.bounds.zone.x[1])) and
            ((pos_y_min.fun >= self.cfg.bounds.zone.y[0]) and (pos_y_max.fun <= self.cfg.bounds.zone.y[1])) and
            ((pos_z_min.fun >= self.cfg.bounds.zone.z[0]) and (pos_z_max.fun <= self.cfg.bounds.zone.z[1]))
        ):
            # TODO Improve
            raise ValueError('Trajectory allowed bounds exceeded')


        
        ## Velocity
        vel_max = sp.optimize.minimize_scalar(
            lambda t: -np.sqrt(
                self.__velocity(t)[0] ** 2 +
                self.__velocity(t)[1] ** 2 + 
                self.__velocity(t)[2] ** 2),
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )

        ### Check successes
        if not vel_max.success:
            # TODO Improve
            raise ValueError('OptimizeException for velocity')

        ### Check bounds
        if np.abs(np.max(vel_max.fun)) >= self.cfg.bounds.max_velocity:
            # TODO Improve
            raise ValueError('Max velocity allowed exceeded')



        ## Acceleration
        acc_max = sp.optimize.minimize_scalar(
            lambda t: -np.sqrt(
                self.__acceleration(t)[0] ** 2 +
                self.__acceleration(t)[1] ** 2 + 
                self.__acceleration(t)[2] ** 2),
            bounds = (0, self.cfg.max_duration),
            method="bounded"
        )
        
        ### Check successes
        if not acc_max.success:
            # TODO Improve
            raise ValueError('OptimizeException for acceleration')

        ### Check bounds
        if np.abs(np.max(acc_max.fun)) >= self.cfg.bounds.max_acceleration:
            # TODO Improve
            raise ValueError('Max acceleration allowed exceeded')



    def position(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration, dt)
        
        return self.__trajectory(t)
    
    def velocity(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration, dt)
        
        return self.__velocity(t)
    
    def acceleration(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration, dt)
        
        return self.__acceleration(t)