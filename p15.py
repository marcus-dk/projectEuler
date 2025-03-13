"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 
routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
import math

def lattice_paths(grid_size):
    return math.comb(2 * grid_size, grid_size)


if __name__ == "__main__":
    print(lattice_paths(20))
