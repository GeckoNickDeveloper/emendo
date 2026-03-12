'''
TODO:
    - Improve code
'''
# Imports
from . import Noise, NoiseConfig
import numpy as np

# Implementation
class BrownNoise(Noise):
    """Brown noise generator"""
    def __init__(self, cfg: NoiseConfig):
        super().__init__(cfg)
    
    
    
    def generate(self, N: int):
    # def generate(self, shape: Tuple[int, int], frequency: float):
        if N is None or N <= 0:
            raise ValueError("Number of samples must be > 0")
        
        # Frequency-domain array (complex)
        X = np.zeros(N, dtype=complex)
        half = N // 2

        # Frequency vector (positive freqs only, excluding DC)
        freqs = np.fft.fftfreq(N, d = 1.0 / self.cfg.freq)
        positive_freqs = freqs[1:half]

        # Random phases
        phases = self.rng.uniform(0, 2*np.pi, half - 1)

        # 1/f magnitude scaling  (Brown noise -> 1/f amplitude)
        magnitude = 1.0 / np.abs(positive_freqs)

        X[1:half] = magnitude * np.exp(1j * phases)

        # Hermitian symmetry
        X[half+1:] = np.conj(X[1:half][::-1])

        # DC = 0
        X[0] = 0.0

        # Nyquist (real)
        X[half] = 0.0
        
        
        # IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal