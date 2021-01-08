# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:29:21 2019

@author: Carlos
"""

def mysum(x, y):
# takes two numbers and returns their sum 
    total = x + y
    return total

#sums two valuees and doubles their sum if they equal each other
def sum_double (x,y):
    if (x == y):
        total = 2*(x + y)
    else:
        total = x + y
    return(total)
    