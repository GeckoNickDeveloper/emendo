# Imports
from dataclasses import dataclass
from typing import Tuple
from numpy import ndarray
from datetime import datetime

# Implementations
@dataclass(frozen = True)
class GeneratorZone:
    x: Tuple[float, float] = (-5_000.0,  5_000.0)   # (min, max)
    y: Tuple[float, float] = (-5_000.0,  5_000.0)   # (min, max)
    z: Tuple[float, float] = (     0.0, 10_000.0)   # (min, max)
    
    def __post_init__(self):
        if (
            self.x[0] < -5_000.0 or self.x[1] >  5_000.0 or
            self.y[0] < -5_000.0 or self.y[1] >  5_000.0 or
            self.z[0] <      0.0 or self.z[1] > 10_000.0
        ):
            raise ValueError('Operational zone bounds exceeded. Bounds cannot exceed (10km x 10km x 10km)')



@dataclass(frozen = True)
class GeneratorBounds:
    max_acceleration: float = 500.0
    max_velocity: float     = 3300.0
    zone: GeneratorZone     = GeneratorZone()
    
    def __post_init__(self):
        if self.max_velocity <= 0.0 or self.max_velocity > 3300.0:
            raise ValueError('Max velocity module cannot exceed `3300.0`ms')
        
        if self.max_acceleration <= 0.0 or self.max_acceleration > 500.0:
            raise ValueError('Max acceleration module cannot exceed `500.0`ms^-2')



@dataclass(frozen = True)
class GeneratorData:
    anchor: Tuple[float, float, float]  = (0.0, 0.0, 0.0) # (lat, lon, alt)
    timestamps: ndarray
    positions: ndarray
    attitudes: ndarray
    date: datetime                      = datetime(2026, 1, 1) # Default date
    
    def __post_init__(self):
        if self.anchor[0] < -90.0 or self.anchor[0] > 90.0:      # Latitude limit
            raise ValueError('Latitude must be included in range (-90.0, 90.0) deg')
        
        if self.anchor[1] < -180.0 or self.anchor[1] > 180.0:    # Longitude limit
            raise ValueError('Longitude must be included in range (-180.0, 180.0) deg')
        
        if self.anchor[2] < 0.0 or self.anchor[2] > 50_000.0:    # Altitude limit: max 50km
            raise ValueError('Altitude must be included in range (0.0, 50000.0) m')
        
        
        if self.timestamps.ndim != 1:
            raise ValueError("`timestamps` must be a 1D ndarray with shape (N)")
        
        if (
            self.positions.ndim != 2 or
            self.positions.shape[1] != 3 or 
            self.positions.shape[0] != self.timestamps.shape[0]
        ):
            raise ValueError("`positions` must be a 2D ndarray with shape (N,3)")
        
        if (
            self.attitudes.ndim != 2 or
            self.attitudes.shape[1] != 3 or 
            self.attitudes.shape[0] != self.timestamps.shape[0]
        ):
            raise ValueError("`attitudes` must be a 2D ndarray with shape (N,3)")
        
        # TODO Add date validation



@dataclass(frozen = True)
class GeneratorConfig:
    bounds: GeneratorBounds = GeneratorBounds()
    data: GeneratorData     = GeneratorData()
    max_duration: float     = 600.0
    kinematic: str          = 'default'
    attitude: str           = 'default'
    magnetic: str           = 'default'
    
    def __post_init__(self):
        if self.max_duration <= 0:
            raise ValueError("`max_duration` must be > 0")
        
        if self.kinematic not in ['default', 'spline']:
            raise ValueError("`kinematic` value must be one of the following: `default`, `spline`")
        
        if self.attitude not in ['default', 'spline']:
            raise ValueError("`attitude` value must be one of the following: `default`")
        
        if self.magnetic not in ['default', 'regular-grid']:
            raise ValueError("`magnetic` value must be one of the following: `default`, `regular-grid`")
            