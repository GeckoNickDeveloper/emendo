# Imports
from ._noise import Noise
from typing import Optional
import numpy as np

# Implementation
class VioletNoise(Noise):
    """Violet noise generator"""
    def __init__(self, fs: float, scale: float = 1.0, seed: Optional[int] = None):
        super().__init__(fs=fs, scale=scale, seed=seed)
    
    
    
    def generate(self, samples: int):
        X = np.zeros(samples, dtype=complex)
        half = samples // 2

        # Frequency vector
        freqs = np.fft.fftfreq(samples, d = self.dt)
        positive_freqs = np.abs(freqs[1:half])

        # Random phases
        phases = self._rng.uniform(0, 2.0 * np.pi, half - 1)

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
        scaling = self.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal