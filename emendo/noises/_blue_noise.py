'''
TODO:
    - Improve code
'''
# Imports
from . import Noise, NoiseConfig
import numpy as np

# Implementation
class BlueNoise(Noise):
    """Blue noise generator"""
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
        phases = self.rng.uniform(0, 2*np.pi, half - 1)

        # Blue noise amplitude scaling: sqrt(f)
        magnitude = np.sqrt(positive_freqs)

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC = 0 (important)
        X[0] = 0.0
        X[half] = 0.0  # Nyquist
        
    
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal