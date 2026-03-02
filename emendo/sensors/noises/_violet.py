# Imports
import numpy as np
from ._noise import Noise

# Implementation
class VioletNoise(Noise):
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
        phases = self.rng_generator.uniform(0, 2.0 * np.pi, half - 1)

        # Violet noise amplitude scaling: f
        magnitude = self.C * positive_freqs

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC must be zero
        X[0] = 0.0
        X[half] = 0.0  # Nyquist
    
    
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        
        # Return noise signal
        return noise_signal