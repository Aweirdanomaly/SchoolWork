# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:45:10 2019

@author: Carlos
"""

#Problem 3 Part 1
def flipside(s):
    """Takes in string 's' and flips its first and second halves,
    if string is odd then the second half has the extra character"""
    l = len(s) // 2
    s = s[l:] + s[:l]
    return(s)
   
#Problem 3 Part 2
def adjust(s, length):
    """ Takes in a string and an integer, and it makes sure
    that that string is the length of the integer, else it
    adds spaces to its left"""
    l = len(s)
    if l >= length :
        return s[:length]
    else:
        dif = length - l
        s = (' ' * dif) + s
        return s
    
    
        
