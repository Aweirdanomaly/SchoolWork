# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:54:58 2019

@author: Carlos
"""

def log(b, n):
    """ takes in integers 'b' and 'n' and returns an integer approximation of
    log(b) n and prints a statement several times"""
    i = 0
    while n > 1:
        m = n
        n = n // b
        print("dividing" , m , "by" , b , "gives" , n)
        i += 1
    return i
        
def add_powers(m, n):
    """ takes in integers 'm' and 'n' and returns the sum of n to all the 
    powers from 0 to m and prints the operational statement a few times"""
    i = 0
    w = 0
    for i in range(m):
        w += (n ** i)
        print(n , "**", i, "=", (n ** i))
        i += i
    return w

def square_evens(values):
    """ takes in a list 'values' and squares whatever elements are even in 
    that list. *Returns nothing*"""
    i = 0
    while i < len(values):
        if values[i] % 2 == 0:
            values[i] *= values[i] 
        i += 1