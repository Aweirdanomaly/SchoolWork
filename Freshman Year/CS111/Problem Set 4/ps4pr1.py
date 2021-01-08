# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:30:05 2019

@author: Carlos
"""


def dec_to_bin(n):
    """takes in integer 'n' and returns its binary counterpart as a string"""
    if n == 0 :
        return '0'
    elif n == 1:
        return '1'
        
    else:
        b = dec_to_bin(n >> 1)
        if n % 2 == 0 :
            return b + '0'
        elif n % 2 == 1:
            return b + '1' 
        
def bin_to_dec(b):
    """takes in binary string 'b' and returns its decimal counterpart"""
    if b == '0' :
        return 0
    elif b == '1':
        return 1
    else:
        a = bin_to_dec(b[0:-1])
        if b[-1] == '1':
            return 2 * a + 1
        else :
            return 2 * a + 0