# API
## Config
from ._generator_config import GeneratorConfig, GeneratorData, GeneratorBounds, GeneratorZone
## Proxy
from ._generator import Generator
## Interfaces
from ._kinematic_generator import KinematicGenerator
from ._attitude_generator import AttitudeGenerator
from ._magnetic_generator import MagneticGenerator
## Implementations
from ._spline_kinematic_generator import SplineKinematicGenerator
from ._regular_grid_magnetic_generator import RegularGridMagneticGenerator



# Export
__all__ = [
    # Classes
    ## Config
    'GeneratorData',    # Sub-configuration class
    'GeneratorBounds',  # Sub-configuration class
    'GeneratorZone',    # Sub-configuration class
    'GeneratorConfig',
    
    ## Proxy
    'Generator',
    
    ## Generators
    ### Interfaces
    'KinematicGenerator',
    'AttitudeGenerator',
    'MagneticGenerator',
    
    ### Implementations
    #### KinematicGenerator
    'SplineKinematicGenerator',
    #### AttitudeGenerator
    #### MagneticGenerator
    'RegularGridMagneticGenerator',
]