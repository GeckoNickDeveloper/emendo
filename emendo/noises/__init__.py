# API
from ._noise import Noise

from ._white import WhiteNoise
from ._brown import BrownNoise
from ._pink import PinkNoise
from ._blue import BlueNoise
from ._violet import VioletNoise

from ._composite import CompositeNoise

# Export
__all__ = [
    # Interface
    'Noise',
    
    # Colored Noise
    'WhiteNoise',
    'BrownNoise',
    'PinkNoise',
    'BlueNoise',
    'VioletNoise',
    
    # Composite Noise
    'CompositeNoise'
]