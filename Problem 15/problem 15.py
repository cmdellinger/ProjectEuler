# -*- coding: UTF-8 -*-

"""
ProjectEuler Problem 15: Lattice paths
Written by cmdellinger

Usage:
  None

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

## ------
## solution
## ------

import time as t

# define X by X grid size
grid_size = 20

# create grid
grid = [[1 for y in range(grid_size+1)] for x in range(grid_size+1)]
grid[0][0] = 0

for i in range(1,grid_size+1):
    for j in range(1,grid_size+1):
        try:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        except:
            pass

print "routes:", grid[-1][-1]

# print runtime of script
print "script runtime:", t.clock()
