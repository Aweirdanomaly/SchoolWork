#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

def inner_grid(height, width):
    """ returns a grid with input height 'height' and width 'width' who
    is composed of 1's everywhere but at the rim of the 2D list"""
    grid = create_grid(height, width)
    
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = 1
    return grid

def random_grid(height, width):
    """ returns a grid with input height 'height' and width 'width' who
    is composed of randomly placed 1's and 0's everywhere but at the
    rim of the 2D list"""
    grid = create_grid(height, width)
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = random.choice([0,1])
    return grid
    
def copy(grid):
    """ takes in a 2D list 'grid' and returns a copy of it"""
    grid_copy = create_grid(len(grid), len(grid[0]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid_copy[r][c] = grid[r][c]
    return grid_copy

def invert(grid):
    """takes in a 2D list 'grid' and turns all its 0 values into 1's
    and vice versa"""
    for r in range(len(grid[0])):
        for c in range(len(grid)):
            if grid[r][c] == 1:
                grid[r][c] = 0
            else :
                grid[r][c] = 1








