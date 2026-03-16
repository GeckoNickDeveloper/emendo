# Imports
from typing import Tuple
import numpy as np

# Implementation
class AHRSEstimator:
    def __init__(self, name: str = 'estimator'):
        if not isinstance(name, str):
            raise TypeError('`name` must be a string')
        
        self.name = name

    def update(self, measurements: Tuple[np.ndarray, np.ndarray, np.ndarray]):
        raise NotImplementedError('`update` method must be implemented')