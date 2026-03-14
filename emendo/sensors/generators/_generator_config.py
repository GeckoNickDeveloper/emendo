# Imports
from dataclasses import dataclass, field
from typing import Tuple, Optional
from datetime import datetime
import numpy as np

# Implementations
@dataclass(frozen = True)
class GeneratorZone:
    x: Tuple[float, float] = (-5_000.0, 5_000.0)   # (min, max)
    y: Tuple[float, float] = (-5_000.0, 5_000.0)   # (min, max)
    z: Tuple[float, float] = (-5_000.0, 5_000.0)   # (min, max)
    
    def __post_init__(self):
        def check_axis(name, axis, min_val, max_val):
            if axis is None:
                raise ValueError(f'{name} cannot be None')
            if len(axis) != 2:
                raise ValueError(f'{name} must have exactly 2 elements')
            if not (min_val <= axis[0] <= max_val):
                raise ValueError(f'{name}[0]={axis[0]} out of bounds [{min_val}, {max_val}]')
            if not (min_val <= axis[1] <= max_val):
                raise ValueError(f'{name}[1]={axis[1]} out of bounds [{min_val}, {max_val}]')

        check_axis('x', self.x, -5_000.0, 5_000.0)
        check_axis('y', self.y, -5_000.0, 5_000.0)
        check_axis('z', self.z, -5_000.0, 5_000.0)



@dataclass(frozen = True)
class GeneratorBounds:
    max_acceleration: float = 500.0
    max_velocity: float     = 3_300.0
    zone: GeneratorZone     = GeneratorZone()
    
    def __post_init__(self):
        def check_param(name, value, min_val, max_val):
            if value is None:
                raise ValueError(f'`{name}` cannot be None')
            if value <= min_val:
                raise ValueError(f'`{name}` must be > {min_val}')
            if value > max_val:
                raise ValueError(f'`{name}` cannot exceed {max_val}')

        check_param('max_velocity', self.max_velocity, 0.0, 3_300.0)
        check_param('max_acceleration', self.max_acceleration, 0.0, 500.0)
        
        if self.zone is None:
            raise ValueError('`zone` cannot be None')
        if not isinstance(self.zone, GeneratorZone):
            raise ValueError('`zone` must be a `GeneratorZone`')
        


@dataclass(frozen = True)
class GeneratorData:
    anchor: Tuple[float, float, float]  = (0.0, 0.0, 0.0) # (lat, lon, alt)
    timestamps: Optional[np.ndarray]    = field(default_factory = lambda: np.array([]))         # shape (N,)
    positions: Optional[np.ndarray]     = field(default_factory = lambda: np.empty((0, 3)))     # shape (N,3)
    attitudes: Optional[np.ndarray]     = field(default_factory = lambda: np.empty((0, 3)))     # shape (N,3)
    date: datetime                      = datetime(2026, 1, 1) # Default date
    
    def __post_init__(self):
        if self.anchor is None:
            raise ValueError('`anchor` cannot be None')
        if len(self.anchor) != 3:
            raise ValueError('`anchor` must have exactly 3 elements')
        
        lat, lon, alt = self.anchor
        if not (-90.0 <= lat <= 90.0):
            raise ValueError('Latitude must be in range [-90, 90] deg')
        if not (-180.0 <= lon <= 180.0):
            raise ValueError('Longitude must be in range [-180, 180] deg')
        if not (0.0 <= alt <= 50_000.0):
            raise ValueError('Altitude must be in range [0, 50000] m')

        if self.timestamps.ndim != 1:
            raise ValueError('`timestamps` must be a 1D ndarray (N,)')

        if self.positions.ndim != 2 or self.positions.shape[1] != 3:
            raise ValueError('`positions` must be 2D ndarray with shape (N,3)')
        if self.positions.shape[0] != self.timestamps.shape[0]:
            raise ValueError('`positions` and `timestamps` must have same length N')

        if self.attitudes.ndim != 2 or self.attitudes.shape[1] != 3:
            raise ValueError('`attitudes` must be 2D ndarray with shape (N,3)')
        if self.attitudes.shape[0] != self.timestamps.shape[0]:
            raise ValueError('`attitudes` and `timestamps` must have same length N')

        # Optional: date validation
        if not isinstance(self.date, datetime):
            raise ValueError('`date` must be a datetime object')



@dataclass(frozen = True)
class GeneratorConfig:
    bounds: GeneratorBounds = field(default_factory = GeneratorBounds)
    data: GeneratorData     = field(default_factory = GeneratorData)
    max_duration: float     = 600.0
    kinematic: str          = 'default'
    attitude: str           = 'default'
    magnetic: str           = 'default'

    def __post_init__(self):
        if self.bounds is None:
            raise ValueError(f'`bounds` cannot be None')
        if not isinstance(self.bounds, GeneratorBounds):
            raise ValueError(f'`bounds` must be `GeneratorBounds`')
        
        if self.data is None:
            raise ValueError(f'`data` cannot be None')
        if not isinstance(self.data, GeneratorData):
            raise ValueError(f'`data` must be `GeneratorData`')
        
        if self.max_duration <= 0:
            raise ValueError('`max_duration` must be > 0')

        def _check_option(name, value, options):
            if value not in options:
                raise ValueError(f'`{name}` must be one of {options}')

        _check_option('kinematic', self.kinematic, ['default', 'spline'])
        _check_option('attitude', self.attitude, ['default', 'spline'])
        _check_option('magnetic', self.magnetic, ['default', 'regular-grid'])
            