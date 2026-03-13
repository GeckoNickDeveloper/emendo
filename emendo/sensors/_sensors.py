# Imports
from . import SensorsConfig
from .generators import Generator
from ..noises import NoiseFactory
import scipy as sp
import numpy as np

# Implementation
class Sensors:
    def __init__(self, cfg: SensorsConfig):
        if cfg is None:
            raise ValueError("`cfg` cannot be None")
        if not isinstance(cfg, SensorsConfig):
            raise ValueError("`cfg` must be a `SensorConfig`")
            
        self.cfg = cfg
        
        # Attributes
        self.generator = Generator(cfg.generator_cfg)
        self.noise = NoiseFactory.create(cfg.noise_cfg)
    
    # Obtain measurements data
    def measurements(self):
        # Timesteps
        dt      = 1.0 / self.cfg.frequency
        dt_os   = 1.0 / (self.cfg.frequency * 20.0)
        
        t       = np.arange(0, self.cfg.max_duration, dt)
        t_os    = np.arange(0, self.cfg.max_duration, dt_os)
        
        # Get true accelerometer (20x oversample)
        wf_gt_pos_os = self.generator.position(t_os)
        wf_gt_acc_os = self.generator.acceleration(t_os)
        # Get true orientation (20x oversample)
        gt_att_os = self.generator.attitude(t_os)
        gt_angular_rate_os = self.generator.angular_rate(t_os)
        # Get true magnetometer (20x oversample)
        wf_gt_mag_os = self.generator.magnetic(wf_gt_pos_os)
        
        # Get noise modeling (20x oversample)
        noise_acc   = self.noise.generate(wf_gt_pos_os.shape, self.cfg.frequency * 20.0)
        noise_gyro  = self.noise.generate(gt_angular_rate_os.shape, self.cfg.frequency * 20.0)
        noise_mag   = self.noise.generate(wf_gt_mag_os.shape, self.cfg.frequency * 20.0)
        
        # Rotate to body frame
        # wf2bf = sp.spatial.transform.RigidTransform(gt_att_os)
        ## Acceleration
        # bf_gt_acc_os = wf2bf.apply(wf_gt_acc_os)
        # bf_gt_acc_os = np.array([r.apply(v) for r, v in zip(gt_att_os, wf_gt_acc_os)])
        bf_gt_acc_os = gt_att_os.apply(wf_gt_acc_os)
        ## Magnetometer
        # bf_gt_mag_os = wf2bf.apply(wf_gt_mag_os)
        # bf_gt_mag_os = np.array([r.apply(v) for r, v in zip(gt_att_os, wf_gt_mag_os)])
        bf_gt_mag_os = gt_att_os.apply(wf_gt_mag_os)
        
        # Add noise        
        ## Accelerometer
        bf_gt_acc_os        += noise_acc
        ## Gyroscope
        gt_angular_rate_os  += noise_gyro
        ## Magnetometer
        bf_gt_mag_os        += noise_mag
        
        # Anti-aliasing filter (optional)
        if not self.cfg.aliasing:
            # Compute coefficients of the Anti-Aliasing filter
            filter = sp.signal.butter(
                3,
                self.cfg.frequency / 2,
                btype = 'lowpass',
                fs = self.cfg.frequency * 20.0)
            
            # Apply the Anti-Aliasing filter
            bf_gt_acc_os = sp.signal.lfilter(
                filter[0],
                filter[1],
                bf_gt_acc_os,
                axis = 0)
            gt_angular_rate_os = sp.signal.lfilter(
                filter[0],
                filter[1],
                gt_angular_rate_os,
                axis = 0)
            bf_gt_mag_os = sp.signal.lfilter(
                filter[0],
                filter[1],
                bf_gt_mag_os,
                axis = 0)
        
        # Downsample (decimation)
        ## Accelerometer
        bf_acc = np.array(bf_gt_acc_os[::20])
        ## Gyroscope
        bf_gyro = np.array(gt_angular_rate_os[::20])
        ## Magnetometer
        bf_mag = np.array(bf_gt_mag_os[::20])
        
        # Return synthetic sensors
        return (bf_acc, bf_gyro, bf_mag)