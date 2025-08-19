"""main.py"""


# Import user-defined functions 
from geometry import compute_sphere_volume


def main():
    """
    Main function to demonstrate the use of compute_sphere_volume.

    This function sets a predefined radius for a sphere, computes its
    volume using the compute_sphere_volume function, and prints the 
    result to the console.
    """
    
    # Define the radius of the sphere (in metres)
    sphere_radius = 5  

    # Compute and print the volume of the sphere
    # f-string formats the output nicely with units
    print(f"Sphere volume: {compute_sphere_volume(sphere_radius)} cubic metres")
    

if __name__=='__main__':
    main()
