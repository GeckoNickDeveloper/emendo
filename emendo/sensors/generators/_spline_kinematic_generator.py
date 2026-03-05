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
                
        # Initialization
        self.__interpolate()
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
        # Optimize Splines & Boundary checking
        ## Position
        pos_x_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[0],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        pos_x_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[0],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        pos_y_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[1],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        pos_y_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[1],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        pos_z_min = sp.optimize.minimize_scalar(
            lambda t: self.__trajectory(t)[2],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        pos_z_max = sp.optimize.minimize_scalar(
            lambda t: -self.__trajectory(t)[2],
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        
        ### Check successes
        if not (
            pos_x_min.success and pos_x_max.success and
            pos_y_min.success and pos_y_max.success and
            pos_z_min.success and pos_z_max.success
        ):
            # TODO Improve
            raise 'OptimizeException for position'
        
        ### Check bounds
        if not (
            ((pos_x_min >= self.config['operation-area']['x']['min']) and ((pos_x_max <= self.config['operation-area']['x']['max']))) and
            ((pos_y_min >= self.config['operation-area']['y']['min']) and ((pos_y_max <= self.config['operation-area']['y']['max']))) and
            ((pos_z_min >= self.config['operation-area']['z']['min']) and ((pos_z_max <= self.config['operation-area']['z']['max'])))
        ):
            # TODO Improve
            raise 'Trajectory allowed bounds exceeded'


        
        ## Velocity
        vel_x_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__velocity(t)[0]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        vel_y_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__velocity(t)[1]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        vel_z_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__velocity(t)[2]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        
        ### Check successes
        if not (vel_x_max.success and vel_y_max.success and vel_z_max.success):
            # TODO Improve
            raise 'OptimizeException for velocity'

        ### Check bounds
        if np.abs(np.max([vel_x_max.fun, vel_y_max.fun, vel_z_max.fun])) * np.sqrt(3) >= self.config['max-velocity']:
            # TODO Improve
            raise 'Max velocity allowed exceeded'



        ## Acceleration
        acc_x_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__acceleration(t)[0]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        acc_y_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__acceleration(t)[1]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        acc_z_max = sp.optimize.minimize_scalar(
            lambda t: -np.abs(self.__acceleration(t)[2]),
            bounds = (self.config['min-time'], self.config['max-time'],),
            method="bounded")
        
        ### Check successes
        if not (acc_x_max.success and acc_y_max.success and acc_z_max.success):
            # TODO Improve
            raise 'OptimizeException for acceleration'

        ### Check bounds
        if np.abs(np.max([acc_x_max.fun, acc_y_max.fun, acc_z_max.fun])) * np.sqrt(3) >= self.config['max-acceleration']:
            # TODO Improve
            raise 'Max acceleration allowed exceeded'



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