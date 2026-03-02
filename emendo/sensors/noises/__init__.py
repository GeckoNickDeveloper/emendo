# API
from .noise import Noise

from .white import WhiteNoise
from .brown import BrownNoise
from .pink import PinkNoise
from .blue import BlueNoise
from .violet import VioletNoise

from .composite import CompositeNoise

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