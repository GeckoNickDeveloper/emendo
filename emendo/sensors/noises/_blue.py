# Imports
import numpy as np
from ._noise import Noise

# Implementation
class BlueNoise(Noise):
    def __init__(self, fs: float, seed: int):
        super().__init__(fs, seed)
        
        self.C = 1.0
    
    
    
    def generate(self, samples: int):
        X = np.zeros(samples, dtype=complex)
        half = samples // 2

        # Frequency vector
        freqs = np.fft.fftfreq(samples, d = self.dt)
        positive_freqs = np.abs(freqs[1:half])

        # Random phases
        phases = self.rng_generator.uniform(0, 2*np.pi, half - 1)

        # Blue noise amplitude scaling: sqrt(f)
        magnitude = self.C * np.sqrt(positive_freqs)

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC = 0 (important)
        X[0] = 0.0
        X[half] = 0.0  # Nyquist
        
    
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        
        # Return noise signal
        return noise_signal