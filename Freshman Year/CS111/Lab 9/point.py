#
# point.py
#
# The beginnings of a class for Point objects
#
# CS 111
#

import math

class Point:
    """ A class for objects that represent points in
        the Cartesian plane.
    """
    
    def __init__(self, init_x, init_y):
        """ constructor for a Point object that represents a point
            with coordinates (init_x, init_y)
        """
        self.x = init_x
        self.y = init_y
        
    def __repr__(self):
        """ returns a string representation for the called Point
            object (self)
            """
        s = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return s

    def distance_from_origin(self):
        """ computes and returns the distance of the called Point object
            (self) from the origin (i.e., from (0, 0))
        """
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist

    def move_down(self, amount):
        """ moves the called Point object (self) in a downwards
            direction by the specified amount
        """
        self.y -= amount

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y >= 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x ==0 or self.y == 0:
            return 0
        else:
            return 4
            
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def flip(self):
        a = self.x * (-1)
        b = self.y *  (-1)
        self.x = b
        self.y = a
        
    def in_same_quadrant(self, other):
        if self.quadrant() == other.quadrant() and self.quadrant() != 0:
            return True
        else:
            return False
        
        
        