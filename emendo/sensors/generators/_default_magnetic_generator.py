'''
TODO:
    - Improve code
'''
# Imports
from . import GeneratorConfig, MagneticGenerator
from scipy.interpolate import RegularGridInterpolator
import numpy as np
import pygeomag as gm

# Implementations
class DefaultMagneticGenerator(MagneticGenerator):
    '''
    MagneticGenerator interface for emendo sensors simulation

    Focused on magnetic field interpolation
    '''
    def __init__(self, cfg: GeneratorConfig):
        super().__init__(cfg)
        
        # Attributes
        self.__field: RegularGridInterpolator

        # Initialization
        self.__interpolate()

    def __interpolate(self):
        # From config
        ## Grid density (^3)
        N = 10
        
        ## Get operational X_min, X_max (longitude)
        x = np.linspace(self.cfg.bounds.zone.x[0], self.cfg.bounds.zone.x[1], N)    # Longitude
        y = np.linspace(self.cfg.bounds.zone.y[0], self.cfg.bounds.zone.y[1], N)    # Latitude
        z = np.linspace(self.cfg.bounds.zone.z[0], self.cfg.bounds.zone.z[1], N)    # Altitude

        # Magnetic Grid
        ## Create magfield grid (WMM)
        V = np.zeros((N, N, N, 3))

        ## Populate grid
        geo = gm.GeoMag()
        dec_time = gm.calculate_decimal_year(self.cfg.data.date)

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    # Compute vector field value at coordinates
                    dlon = np.rad2deg(x[i] / 6_371_000.0)
                    dlat = np.rad2deg(y[i] / 6_371_000.0)
                    
                    # TODO implement real reading
                    t_lat = self.cfg.data.anchor[0] + dlat
                    t_lon = self.cfg.data.anchor[1] + dlon
                    t_alt = self.cfg.data.anchor[2] + z[i]

                    res = geo.calculate(
                        t_lat,
                        t_lon,
                        t_alt,
                        dec_time
                    )

                    # Convert from NED to ENU
                    V[i,j,k] = np.array([ res.y, res.x, -res.z ])

        # Obtain Interpolating function
        self.__field = RegularGridInterpolator(
            (x, y, z),
            V,
            method = 'cubic',
            bounds_error = False,
            fill_value = None
        )



    def magnetic(self, positions: np.ndarray) -> np.ndarray:
        if positions is None:
            raise ValueError('`positions` cannot be None')
        if positions.ndim != 2 or positions.shape[1] != 3:
            raise ValueError('`positions` must be 2D ndarray with shape (N, 3)')
        
        min_pos = np.min(positions, axis = 0) # (x, y, z)
        max_pos = np.max(positions, axis = 0) # (x, y, z)

        if (
            min_pos[0] < self.cfg.bounds.zone.x[0] or max_pos[0] > self.cfg.bounds.zone.x[1] or 
            min_pos[1] < self.cfg.bounds.zone.y[0] or max_pos[1] > self.cfg.bounds.zone.y[1] or 
            min_pos[2] < self.cfg.bounds.zone.z[0] or max_pos[2] > self.cfg.bounds.zone.z[1]
        ):
            raise ValueError('`positions` must not exceed configuration bounds')
        
        return self.__field(positions)