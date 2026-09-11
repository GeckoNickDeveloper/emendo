# Imports
from . import AHRSEstimator
from typing import Tuple
import numpy as np

# Implementation
class SAAM(AHRSEstimator):
    def __init__(self):
        super().__init__(name = 'saam')

    def update(self, measurements: Tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
        # Validation
        if measurements is None:
            raise ValueError('`measurements` cannot be None')
        if len(measurements) != 3:
            raise ValueError('`measurements` must contain 3 elements')
        if (
            (not isinstance(measurements[0], np.ndarray)) or
            (not isinstance(measurements[1], np.ndarray)) or
            (not isinstance(measurements[2], np.ndarray))
        ):
            raise TypeError('`measurements` must contain 3 numpy array')
        if (
            measurements[0].shape[1] != 3 or
            measurements[1].shape[1] != 3 or
            measurements[2].shape[1] != 3
        ):
            raise ValueError('`measurements` items must have the shapes (N, 3)')
        if (
            measurements[0].shape != measurements[1].shape or
            measurements[0].shape != measurements[2].shape
        ):
            raise ValueError('`measurements` items must have the same shapes')
        
        # Implementation
        acc, _, mag = measurements
        
        ## Compute norms
        acc_norm = np.linalg.norm(acc, axis = 1)
        mag_norm = np.linalg.norm(mag, axis = 1)

        ## Handle NaNs
        if not (np.all(acc_norm > 0)) and (np.all(mag_norm > 0)):
            return None
        
        ## Normalize
        acc /= acc_norm.reshape(-1, 1)
        mag /= mag_norm.reshape(-1, 1)

        mD = acc[:, 0] * mag[:, 0] + acc[:, 1] * mag[:, 1] + acc[:, 2] * mag[:, 2]
        mN = np.sqrt(1 - mD ** 2)

        q = np.stack([
            -acc[:, 1] * (mN + mag[:, 0]) + acc[:, 0] * mag[:, 1],
            (acc[:, 2] - 1) * (mN + mag[:, 0]) + acc[:, 0] * (mD - mag[:, 2]),
            (acc[:, 2] - 1) * mag[:, 1] + acc[:, 1] * (mD - mag[:, 2]),
            acc[:, 2] * mD - acc[:, 0] * mN - mag[:, 2]
        ], axis = 1)
        
        # Normalize q
        q /= np.linalg.norm(q, axis = 1, keepdims = True)

        return q

'''function q = SAAM(Ab, Mb)

    ax = Ab(1);       ay = Ab(2);       az = Ab(3);
    mx = Mb(1);       my = Mb(2);       mz = Mb(3);

    mD = ax * mx + ay * my + az * mz;
    mN = sqrt(1 - mD * mD);

    q = [- ay * (mN + mx) + ax * my;
         (az - 1) * (mN + mx) + ax * (mD - mz);
         (az - 1) * my + ay * (mD - mz);
         az * mD - ax * mN - mz];
    
    q = q ./ norm(q);
end'''