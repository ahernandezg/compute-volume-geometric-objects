"""geometry.py"""

# Import standard libraries
import numpy as np


def compute_sphere_volume(sphere_radius:float)->float:
    """
    Compute the volume of a sphere given its radius.

    Parameters
    ----------
    sphere_radius : float
        The radius of the sphere (must be a non-negative value).

    Returns
    -------
    float
        The volume of the sphere calculated using the formula:
        V = (4/3) * π * r^3

    Raises
    ------
    ValueError
        If the input radius is negative.
    """
    
    # Validate input to avoid negative radius values
    if sphere_radius < 0:
        raise ValueError("Radius cannot be negative")

    # Formula: V = 4/3 * π * r³
    return (4/3) * np.pi * sphere_radius**3