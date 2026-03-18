# Imports
import emendo as E
import pytest
import numpy as np



# Tests
def test_saam_shape():
    saam = E.ahrs.estimators.SAAM()

    res = saam.update((np.ones((2, 3)), np.ones((2, 3)), np.ones((2, 3))))
    
    assert res.shape == (2, 4)