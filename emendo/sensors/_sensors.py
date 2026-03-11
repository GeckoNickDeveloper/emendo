# Imports
from . import SensorsConfig
from .generators import Generator
from ..noises import NoiseFactory
import numpy as np

# Implementation
class Sensors:
    def __init__(self, cfg: SensorsConfig):
        if cfg is None:
            raise ValueError("Configuration can't be None")
            
        self.cfg = cfg
        
        # Attributes
        self.generator = Generator(cfg.generator_cfg)
        self.noise = NoiseFactory.create(cfg.noise_cfg)
    
    # Obtain measurements data
    def measurements(self):
        # Timesteps
        dt      = 1.0 / self.cfg.frequency
        dt_os   = 1.0 / (self.cfg.frequency * 20)
        
        t       = np.arange(0, self.cfg.max_duration + dt / 2.0, dt)
        t_os    = np.arange(0, self.cfg.max_duration + dt_os / 2.0, dt_os)
        
        # Get true accelerometer (20x oversample)
        # Get true orientation (20x oversample)
        # Get true magnetometer (20x oversample)
        
        # Get noise modeling (20x oversample)
        noise_acc_x = self.noise.generate(t.shape[0])
        noise_acc_y = self.noise.generate(t.shape[0])
        noise_acc_z = self.noise.generate(t.shape[0])
        
        # Rotate to body frame
        # Add noise
        noise = self.noise.generate()
        
        # Anti-aliasing filter (optional)
        if not self.cfg.aliasing:
            pass
        
        # Downsample (decimation)
        pass