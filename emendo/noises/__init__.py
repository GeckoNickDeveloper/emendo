# API
## Config
from ._noise_config import NoiseConfig
## Proxy
from ._noise_factory import NoiseFactory
## Interfaces
from ._noise import Noise
## Implementations
from ._brown import BrownNoise
from ._pink import PinkNoise
from ._white import WhiteNoise
from ._blue import BlueNoise
from ._violet import VioletNoise



# Export
__all__ = [
    # Modules
    ## NO MODULES

    # Classes
    ## Config
    'NoiseConfig',
    ## Factory
    'NoiseFactory',
    ## Interface
    'Noise',
    ## Implementations
    'BrownNoise',
    'PinkNoise',
    'WhiteNoise',
    'BlueNoise',
    'VioletNoise',
]