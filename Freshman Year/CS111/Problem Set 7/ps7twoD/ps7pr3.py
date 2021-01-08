#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random


def count_neighbors(cellr, cellc, grid):
    """ takes in 2 integers and a 2D list as inputs 'cellr', 'cellc', and
    'grid' and returns the amount of 1's immediately sorrounding 
    grid[cellr][cellc] """
    count = 0
    for r in range(cellr - 1, cellr + 2):
        for c in range(cellc - 1, cellc + 2):
            if grid[r][c] == 1 :   
                    count += 1
    if grid[cellr][cellc] == 1:
        count -= 1
    return count

def next_gen(grid):
    """Takes in a 2D list 'grid', applies the rules of Conway's game of
    life to it and returns the resulting 2D list"""
    new_grid = copy(grid)
    for r in range(1, len(new_grid)-1):
        for c in range(1, len(new_grid[0])-1):
            if count_neighbors(r, c, grid) < 2 or count_neighbors(r, c, grid) > 3:
                new_grid[r][c] = 0
            elif count_neighbors(r, c, grid) == 3 and new_grid[r][c] == 0:
                new_grid[r][c] = 1
    
    return new_grid