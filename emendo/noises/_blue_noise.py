# Imports
from . import Noise, NoiseConfig
from typing import Tuple
import numpy as np

# Implementation
class BlueNoise(Noise):
    """Blue noise generator"""
    def __init__(self, cfg: NoiseConfig):
        super().__init__(cfg)
    
    # def generate(self, N: int):
    def generate(self, shape: Tuple[int, int], frequency: float) -> np.ndarray:
        # Validation
        if shape is None:
            raise ValueError('`shape` cannot be None')
        if len(shape) != 2:
            raise ValueError('`shape` must contain 2 elements')
        if (
            shape[0] is None or shape[0] <= 0 or
            shape[1] is None or shape[1] <= 0
        ):
            raise ValueError('`shape` elements must be > 0')
        
        if frequency is None:
            raise ValueError('`frequency` cannot be None')
        if frequency <= 0:
            raise ValueError('`frequency` must be > 0')
        


        # Actual Noise implementation
        ## Create noise spectrum array
        X = np.zeros(shape[0], dtype=complex)

        ## Positive frequencies (excluding DC and Nyquist)
        half = shape[0] // 2

        ## Get signal frequencies
        freqs = np.fft.fftfreq(
            shape[0],
            d = 1.0 / frequency
        )
        positive_freqs = np.abs(freqs[1:half])

        ## Noise spectrum building
        ### Generate random phases
        phases = self.rng.uniform(
            0.0,
            2.0 * np.pi,
            (half - 1, shape[1])
        )

        ### Blue noise amplitude scaling: sqrt(f)
        magnitude = np.sqrt(positive_freqs)

        ### Set positive-frequency bins
        X[1:half, :] = magnitude * np.exp(1j * phases)

        ### Hermitian symmetry
        X[half + 1:, :] = np.conj(X[1:half, :][::-1])

        ## Finalize spectrum
        ### Zero-mean signal (DC)
        X[0, :] = 0.0
        ### Nyquist frequency
        X[half, :] = 0.0
        
    
        ## IFFT to create noise signal
        noise_signal = np.fft.ifft(X).real
        scaling = self.cfg.scale / np.std(noise_signal)
        noise_signal *= scaling
        
        # Return noise signal
        return noise_signal