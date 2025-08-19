import pytest 
from geometry.geometry import compute_sphere_volume
import numpy as np

def test_compute_sphere_volume():
    sphere_radius = 3
    expected = 4/3 * np.pi * sphere_radius**3
    assert np.isclose(compute_sphere_volume(sphere_radius), expected)