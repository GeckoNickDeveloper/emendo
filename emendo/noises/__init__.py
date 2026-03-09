# API
## Config
from ._noise_config import NoiseConfig
## Proxy
from ._noise_proxy import NoiseProxy
## Interfaces
from ._base_noise import BaseNoise
## Implementations
from ._white import WhiteNoise
from ._brown import BrownNoise
from ._pink import PinkNoise
from ._blue import BlueNoise
from ._violet import VioletNoise
from ._composite import CompositeNoise



# Export
__all__ = [
    # Modules

    # Classes
    ## Config
    'NoiseConfig',

    ## Proxy
    'NoiseProxy',

    ## Interface
    'BaseNoise',
    
    ## Implementations
    'WhiteNoise',
    'BrownNoise',
    'PinkNoise',
    'BlueNoise',
    'VioletNoise',
    'CompositeNoise'
]