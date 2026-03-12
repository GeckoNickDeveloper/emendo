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
    def position(self, start, freq, duration):
        return self.__kinematic.position(start, freq, duration)

    def velocity(self, start, freq, duration):
        return self.__kinematic.velocity(start, freq, duration)

    def acceleration(self, start, freq, duration):
        return self.__kinematic.acceleration(start, freq, duration)

    # Attitude
    def attitude(self, start, freq, duration):
        return self.__attitude.attitude(start, freq, duration)
    
    def angular_rate(self, start, freq, duration):
        return self.__attitude.angular_rate(start, freq, duration)

    # Magnetic
    def magnetic(self, positions):
        return self.__magnetic.magnetic(positions)