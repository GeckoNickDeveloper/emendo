# Imports
from . import (
    GeneratorConfig,
    KinematicGenerator,
    AttitudeGenerator,
    MagneticGenerator,
    SplineKinematicGenerator,
    RegularGridMagneticGenerator,
    RotationSplineAttitudeGenerator,
)


# Implementation
class Generator:
    _kinematic_map = {
        "default": SplineKinematicGenerator,
        "spline": SplineKinematicGenerator,
    }

    _attitude_map = {
        "default": RotationSplineAttitudeGenerator,
        "rotation-spline": RotationSplineAttitudeGenerator,
    }

    _magnetic_map = {
        "default": RegularGridMagneticGenerator,
        "regular-grid": RegularGridMagneticGenerator,
    }

    def __init__(self, cfg: GeneratorConfig):
        if cfg is None:
            raise ValueError('`GeneratorConfig` cannot be None')
        
        self.config = cfg

        # Generator selectors
        self.__kinematic: KinematicGenerator = self._kinematic_map[cfg.kinematic](cfg)
        self.__attitude: AttitudeGenerator  = self._attitude_map[cfg.attitude](cfg)
        self.__magnetic: MagneticGenerator  = self._magnetic_map[cfg.magnetic](cfg)



    def position(self, start, freq, duration):
        return self.__kinematic.position(start, freq, duration)

    def velocity(self, start, freq, duration):
        return self.__kinematic.velocity(start, freq, duration)

    def acceleration(self, start, freq, duration):
        return self.__kinematic.acceleration(start, freq, duration)

    def attitude(self, start, freq, duration):
        return self.__attitude.attitude(start, freq, duration)
    
    def angular_rate(self, start, freq, duration):
        return self.__attitude.angular_rate(start, freq, duration)

    def magnetic(self, positions):
        return self.__magnetic.magnetic(positions)