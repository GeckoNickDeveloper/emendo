import pytest
import numpy as np
from emendo.sensors.generators import RegularGridMagneticGenerator, GeneratorConfig

def test_regular_grid_magnetic_generator_init_defaults(monkeypatch):
    cfg = GeneratorConfig()
    
    # Patch pygeomag.GeoMag to prevent real calculations
    class DummyGeoMag:
        def calculate(self, lat, lon, alt, dec_time):
            class Result:
                x = 0.0
                y = 0.0
                z = 0.0
            return Result()
        @staticmethod
        def calculate_decimal_year(date):
            return 2026.0
    monkeypatch.setattr("pygeomag.GeoMag", lambda: DummyGeoMag())
    
    mg = RegularGridMagneticGenerator(cfg)
    assert hasattr(mg, "magnetic")
    
def test_regular_grid_magnetic_generator_magnetic(monkeypatch):
    cfg = GeneratorConfig()
    
    # Patch pygeomag.GeoMag to prevent real calculations
    class DummyGeoMag:
        def calculate(self, lat, lon, alt, dec_time):
            class Result:
                x = 1.0
                y = 2.0
                z = 3.0
            return Result()
        @staticmethod
        def calculate_decimal_year(date):
            return 2026.0
    monkeypatch.setattr("pygeomag.GeoMag", lambda: DummyGeoMag())
    
    mg = RegularGridMagneticGenerator(cfg)
    positions = np.array([[0.0,0.0,0.0]])
    output = mg.magnetic(positions)
    assert output.shape[0] == positions.shape[0]