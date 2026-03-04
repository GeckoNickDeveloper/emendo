# Imports
from . import Noise

from typing import Optional
import numpy as np



# Implementation
class WhiteNoise(Noise):
    """White noise generator"""
    def __init__(self, fs: float, scale: float = 1.0, seed: Optional[int] = None):
        super().__init__(fs=fs, scale=scale, seed=seed)
    
    
    
    def generate(self, samples: int):
        # Noise spectrum
        X = np.zeros(samples, dtype = complex)

        # Positive frequencies (excluding DC and Nyquist)
        half = samples // 2

        # Random phases
        phases = self._rng.uniform(0, 2 * np.pi, half - 1)

        # Set positive-frequency bins
        X[1:half] = np.exp(1.0j * phases)

        # Enforce Hermitian symmetry for real signal
        X[half+1:] = np.conj(X[1:half][::-1])

        # Set DC = 0
        # Zero-mean signal
        X[0] = 0.0

        # Nyquist frequency (must be real if N is even)
        X[half] = 1.0
        
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal