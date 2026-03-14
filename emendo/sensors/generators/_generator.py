# Imports
from . import (
    GeneratorConfig,
    KinematicGenerator,
    AttitudeGenerator,
    MagneticGenerator,
    DefaultKinematicGenerator,
    DefaultMagneticGenerator,
    DefaultAttitudeGenerator,
)
import numpy as np


# Implementation
class Generator:
    _kinematic_map = {
        "default": DefaultKinematicGenerator,
    }

    _attitude_map = {
        "default": DefaultAttitudeGenerator,
    }

    _magnetic_map = {
        "default": DefaultMagneticGenerator,
    }

    def __init__(self, cfg: GeneratorConfig):
        if cfg is None:
            raise ValueError('`GeneratorConfig` cannot be None')
        
        self.config = cfg

        # Generator selectors
        self.__kinematic: KinematicGenerator = self._kinematic_map[cfg.kinematic](cfg)
        self.__attitude: AttitudeGenerator  = self._attitude_map[cfg.attitude](cfg)
        self.__magnetic: MagneticGenerator  = self._magnetic_map[cfg.magnetic](cfg)


    # Trajectory
    def position(self, timesteps: np.ndarray):
        return self.__kinematic.position(timesteps)

    def velocity(self, timesteps: np.ndarray):
        return self.__kinematic.velocity(timesteps)

    def acceleration(self, timesteps: np.ndarray):
        return self.__kinematic.acceleration(timesteps)

    # Attitude
    def attitude(self, timesteps: np.ndarray):
        return self.__attitude.attitude(timesteps)
    
    def angular_rate(self, timesteps: np.ndarray):
        return self.__attitude.angular_rate(timesteps)

    # Magnetic
    def magnetic(self, positions: np.ndarray):
        return self.__magnetic.magnetic(positions)