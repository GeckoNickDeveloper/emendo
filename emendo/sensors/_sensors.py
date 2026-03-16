# Imports
from . import SensorsConfig
from .generators import Generator
from ..noises import NoiseFactory
from typing import Tuple
import numpy as np
import scipy as sp

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
    
    def positions(self) -> np.ndarray:
        # Timesteps
        dt  = 1.0 / self.cfg.frequency
        t   = np.arange(0, self.cfg.max_duration, dt)
        
        # Get true attitude
        positions = self.generator.position(t)
        
        # Return true attitude as quaternion
        return positions
    
    def velocities(self) -> np.ndarray:
        # Timesteps
        dt  = 1.0 / self.cfg.frequency
        t   = np.arange(0, self.cfg.max_duration, dt)
        
        # Get true attitude
        velocities = self.generator.velocity(t)
        
        # Return true attitude as quaternion
        return velocities
    
    def attitudes(self) -> np.ndarray:
        # Timesteps
        dt  = 1.0 / self.cfg.frequency
        t   = np.arange(0, self.cfg.max_duration, dt)
        
        # Get true attitude
        attitude = self.generator.attitude(t)
        
        # Return true attitude as quaternion
        return attitude.as_quat()
    
    # Obtain measurements data
    def measurements(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Timesteps
        dt_os   = 1.0 / (self.cfg.frequency * 20.0)
        t_os    = np.arange(0, self.cfg.max_duration, dt_os)
        
        # Get true signal (20x overasample)
        ## Position Accelerometer (20x oversample)
        wf_gt_pos_os = self.generator.position(t_os)
        wf_gt_acc_os = self.generator.acceleration(t_os)
        ## Orientation and Gyroscope (20x oversample)
        gt_att_os = self.generator.attitude(t_os)
        gt_angular_rate_os = self.generator.angular_rate(t_os)
        ## Magnetometer (20x oversample)
        wf_gt_mag_os = self.generator.magnetic(wf_gt_pos_os)
        
        # Get noise modeling (20x oversample)
        noise_acc   = self.noise.generate(wf_gt_pos_os.shape, self.cfg.frequency * 20.0)
        noise_gyro  = self.noise.generate(gt_angular_rate_os.shape, self.cfg.frequency * 20.0)
        noise_mag   = self.noise.generate(wf_gt_mag_os.shape, self.cfg.frequency * 20.0)
        
        # Rotate to body frame
        ## Acceleration
        bf_gt_acc_os = gt_att_os.apply(wf_gt_acc_os)
        ## Magnetometer
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
        
        # Add biases
        ## Accelerometer
        ### Add gravity
        bf_acc[:,2] += 9.81
        ## Gyroscope
        bf_gyro[:] += np.deg2rad(np.array([2, 1.4, 7]))
        ## Magnetometer
        
        # Return synthetic sensors
        return (bf_acc, bf_gyro, bf_mag)