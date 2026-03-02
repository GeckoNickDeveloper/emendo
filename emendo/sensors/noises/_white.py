# Imports
import numpy as np
from ._noise import Noise

# Implementation
class WhiteNoise(Noise):
    def __init__(self, fs: float, seed: int):
        super().__init__(fs, seed)
        
        self.C = 1.0
    
    
    
    def generate(self, samples: int):
        # Noise spectrum
        X = np.zeros(samples, dtype = complex)

        # Positive frequencies (excluding DC and Nyquist)
        half = samples // 2

        # Random phases
        phases = self.rng_generator.uniform(0, 2 * np.pi, half - 1)

        # Set positive-frequency bins
        X[1:half] = self.C * np.exp(1.0j * phases)

        # Enforce Hermitian symmetry for real signal
        X[half+1:] = np.conj(X[1:half][::-1])

        # Set DC = 0
        # Zero-mean signal
        X[0] = 0.0

        # Nyquist frequency (must be real if N is even)
        X[half] = self.C
        
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        
        # Return noise signal
        return noise_signal