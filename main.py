import numpy as np


def compute_sphere_volume(sphere_radius:float)->float:
    return 4/3 * np.pi *sphere_radius**3


def main():
    sphere_radius = 5
    print(f"Sphere volume: {compute_sphere_volume(sphere_radius)} cubic metres")
    
if __name__=='__main__':
    main()
    