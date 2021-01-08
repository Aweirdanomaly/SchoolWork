# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:37:54 2019

@author: Carlos
"""

# Problem 4 part 1
def copy(s, n):
    """takes in string 's' and integer 'n' and copies 's' 'n' times"""
    if n <= 0:
        return ''
    else:
        
        b = copy(s, n-1)
        return b + s
        
#Problem 4 part 2
def compare(list1, list2):
    """ takes in two lists 'list1' and 'list2' and returns how
    many values in 'list1' are less than those in 'list2'"""
    if list1 == [] or list2 == []:
        return 0
    else:
        b = compare(list1[1:], list2[1:])
        if list1[0] < list2[0]:
            return b+1 
        else:
            return b
        
#Problem 4 part 3
def double(s):
    """ takes in string 's' and copies all of its characters
    nest to the original ones """
    if s == '':
        return ''
    else:
        b = double(s[0:-1]) 
        return s[-1] + s[-1]