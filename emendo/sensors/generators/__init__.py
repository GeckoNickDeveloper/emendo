# API
## Config
from ._generator_config import GeneratorConfig, GeneratorData, GeneratorBounds, GeneratorZone
## Interfaces
from ._kinematic_generator import KinematicGenerator
from ._attitude_generator import AttitudeGenerator
from ._magnetic_generator import MagneticGenerator
## Implementations
from ._spline_kinematic_generator import SplineKinematicGenerator
from ._rotation_spline_attitude_generator import RotationSplineAttitudeGenerator
from ._regular_grid_magnetic_generator import RegularGridMagneticGenerator
## Proxy
from ._generator import Generator


# Export
__all__ = [
    # Classes
    ## Config
    'GeneratorData',    # Sub-configuration class
    'GeneratorBounds',  # Sub-configuration class
    'GeneratorZone',    # Sub-configuration class
    'GeneratorConfig',
    
    ## Generators
    ### Interfaces
    'KinematicGenerator',
    'AttitudeGenerator',
    'MagneticGenerator',
    
    ### Implementations
    #### KinematicGenerator
    'SplineKinematicGenerator',
    #### AttitudeGenerator
    'RotationSplineAttitudeGenerator',
    #### MagneticGenerator
    'RegularGridMagneticGenerator',

    ## Proxy
    'Generator',
]