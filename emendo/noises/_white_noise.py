'''
TODO:
    - Improve code
'''
# Imports
from . import Noise, NoiseConfig
import numpy as np

# Implementation
class WhiteNoise(Noise):
    """White noise generator"""
    def __init__(self, cfg: NoiseConfig):
        super().__init__(cfg)
    
    
    
    def generate(self, N: int):
        if N is None or N <= 0:
            raise ValueError("Number of samples must be > 0")
        
        # Noise spectrum
        X = np.zeros(N, dtype = complex)

        # Positive frequencies (excluding DC and Nyquist)
        half = N // 2

        # Random phases
        phases = self.rng.uniform(0, 2 * np.pi, half - 1)

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
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal