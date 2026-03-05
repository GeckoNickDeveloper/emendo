# Imports
from . import GeneratorConfig
from . import KinematicGenerator

import scipy as sp
import numpy as np



# Implementations
class SplineKinematicGenerator(KinematicGenerator):
    '''
    SplineKinematicGenerator for emendo sensors simulation

    Based on splines
    '''
    def __init__(self, config: GeneratorConfig):
        super().__init__(config)
        
        # Attributes
        self.__trajectory: sp.interpolate.BSpline
        self.__velocity: sp.interpolate.BSpline
        self.__acceleration: sp.interpolate.BSpline
        
        # Attributes
        self.__limits: tuple[float, float]
        
        # Initialization
        self.__interpolate()
        self.__bounds()
        self.__validate()
    
    
    
    def __interpolate(self):
        bc = ([(2, np.zeros(3))], [(2, np.zeros(3))])
        self.__trajectory = sp.interpolate.make_interp_spline(
            self.config['data']['timestamps'],
            self.config['data']['posiotions'],
            k = 3,
            bc_type = bc
        )
        
        self.__velocity = self.__trajectory.derivative(1)
        self.__acceleration = self.__trajectory.derivative(2)
    
    def __validate(self):
        # Optimize Splines
        ## Velocity
        vel_x_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[0], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        vel_y_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[1], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        vel_z_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[2], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        
        ## Acceleration
        acc_x_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[0], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        acc_y_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[1], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        acc_z_max = sp.optimize.minimize_scalar(lambda t: -self.__velocity(t)[2], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        
        # Check successes
        if not (
            vel_x_max.success and vel_y_max.success and vel_z_max.success and
            acc_x_max.success and acc_y_max.success and acc_z_max.success
        ):
            # TODO Improve
            raise 'OptimizeException'
        
        # Max velocity bound
        if np.abs(np.max([vel_x_max.fun, vel_y_max.fun, vel_z_max.fun])) * np.sqrt(3) >= self.config['max-velocity']:
            # TODO Improve
            raise 'Max velocity allowed exceeded'
        
        # Max acceleration bound
        if np.abs(np.max([acc_x_max.fun, acc_y_max.fun, acc_z_max.fun])) * np.sqrt(3) >= self.config['max-acceleration']:
            # TODO Improve
            raise 'Max acceleration allowed exceeded'
            
        
        
    
    def __bounds(self):
        # Optimize Splines
        ## X
        x_min = sp.optimize.minimize_scalar(lambda t: self.__trajectory(t)[0], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        x_max = sp.optimize.minimize_scalar(lambda t: -self.__trajectory(t)[0], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        ## Y
        y_min = sp.optimize.minimize_scalar(lambda t: self.__trajectory(t)[1], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        y_max = sp.optimize.minimize_scalar(lambda t: -self.__trajectory(t)[1], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        ## Z
        z_min = sp.optimize.minimize_scalar(lambda t: self.__trajectory(t)[2], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        z_max = sp.optimize.minimize_scalar(lambda t: -self.__trajectory(t)[2], bounds = (self.config['min-time'], self.config['max-time'],), method="bounded")
        
        # Check successes
        if not (
            x_min.success and x_max.success and
            y_min.success and y_max.success and
            z_min.success and z_max.success
        ):
            # TODO Improve
            raise 'OptimizeException'
        
        self.__limits = [
            (x_min.fun, x_max.fun),
            (y_min.fun, y_max.fun),
            (z_min.fun, z_max.fun),
        ]



    def limits(self):
        return self.__limits

    def position(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration / dt + 1e-9, dt)
        
        return self.__trajectory(t)
    
    def velocity(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration / dt + 1e-9, dt)
        
        return self.__velocity(t)
    
    def acceleration(self, start: float, freq: float, duration: float):
        # TODO Add check of simulation bounds exceeded
        dt = 1.0 / freq
        t = np.arange(start, start + duration / dt + 1e-9, dt)
        
        return self.__acceleration(t)