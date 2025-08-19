import pytest 
from geometry.geometry import compute_sphere_volume
import numpy as np

def test_compute_sphere_volume():
    # Sphere radius = 1 
    sphere_radius = 1
    expected = 4/3 * np.pi * sphere_radius**3
    assert np.isclose(compute_sphere_volume(1), expected)