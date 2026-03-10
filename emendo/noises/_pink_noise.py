# Imports
from . import Noise, NoiseConfig
import numpy as np

# Implementation
class PinkNoise(Noise):
    """Pink noise generator"""
    def __init__(self, cfg: NoiseConfig):
        super().__init__(cfg)
    
    
    
    def generate(self, N: int):
        X = np.zeros(N, dtype=complex)
        half = N // 2

        # Frequency vector
        freqs = np.fft.fftfreq(N, d = 1.0 / self.cfg.freq)
        positive_freqs = np.abs(freqs[1:half])

        # Random phases
        phases = self.rng.uniform(0, 2*np.pi, half - 1)

        # Pink noise amplitude scaling: 1/sqrt(f)
        magnitude = 1.0 / np.sqrt(positive_freqs)

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC = 0
        X[0] = 0.0
        X[half] = 0.0  # Nyquist (real)
    
    
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal