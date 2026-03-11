'''
TODO:
    - Improve code
'''
# Imports
from . import Noise, NoiseConfig
import numpy as np

# Implementation
class VioletNoise(Noise):
    """Violet noise generator"""
    def __init__(self, cfg: NoiseConfig):
        super().__init__(cfg)
    
    def generate(self, N: int):
        if N is None or N <= 0:
            raise ValueError("Number of samples must be > 0")
        
        X = np.zeros(N, dtype=complex)
        half = N // 2

        # Frequency vector
        freqs = np.fft.fftfreq(N, d = 1.0 / self.cfg.freq)
        positive_freqs = np.abs(freqs[1:half])

        # Random phases
        phases = self.rng.uniform(0, 2.0 * np.pi, half - 1)

        # Violet noise amplitude scaling: f
        magnitude = positive_freqs

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC must be zero
        X[0] = 0.0
        X[half] = 0.0  # Nyquist
    
    
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal