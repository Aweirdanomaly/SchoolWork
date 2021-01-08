# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
    

def cube(x):
    """ takes a numberr and multiplies it by itself 3 times"""
    return x**3
    
def convert_to_inches(yards, feet):
    """takes inputs yards and feet
    and then returns the corresponding length in inches"""
    if yards < 0:
        yards = 0
    if feet < 0:
        feet = 0
    return 36*(yards) + 12*(feet)

def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """takes inputs of height and width in yards and feet
    calls convert_to_inches to turn them into inches and then
    multiplies them to get the area"""
    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)
    return height * width

def median(a, b, c):
    """ returns the middle value of 3 inputs: a, b, c"""
    if a <= b <= c:
        return b
    elif b <= a <= c:
        return a
    elif a <= c <= b:
        return c
    elif c <= b <= a:
        return b
    elif c <= a <= b:
        return a
    elif b <= c <= a:
        return c
    





# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
