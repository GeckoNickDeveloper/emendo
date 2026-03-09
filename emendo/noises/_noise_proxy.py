# Imports
from . import NoiseConfig
from . import BaseNoise

from typing import List

from . import *


import numpy as np

# Implementations
class NoiseProxy():
    '''
    Noise API for emendo sensor simulation
    '''

    def __init__(self, config: List[NoiseConfig]):
        self.config = config
        
        self.__noise: BaseNoise

        # Selector for noise
        if len(self.config > 1):
            self.__noise = CompositeNoise([])

            for cfg in self.config:
                self.__noise.add(self.__get_noise(cfg))

        else:
            self.__noise = self.__get_noise(cfg)
    


    def __get_noise(self, cfg: NoiseConfig):
        if cfg.name == 'white':
            return WhiteNoise(cfg)
        elif cfg.name == 'brown':
            return BrownNoise(cfg)
        elif cfg.name == 'pink':
            return PinkNoise(cfg)
        elif cfg.name == 'blue':
            return BlueNoise(cfg)
        elif cfg.name == 'violet':
            return VioletNoise(cfg)
        else:
            raise ValueError('Unknown noise type')

    def generate(self, samples: int) -> np.ndarray:
        return self.__noise.generate(samples)