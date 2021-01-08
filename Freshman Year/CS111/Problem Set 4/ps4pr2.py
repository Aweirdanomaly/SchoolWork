# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 02:13:26 2019

@author: Carlos
"""
from ps4pr1 import *
def add(b1, b2):
    "takes in binary strings 'b1' and 'b2' and returns their binary sum"""
    b1 = bin_to_dec(b1)
    b2 = bin_to_dec(b2)
    
    bres = b1 + b2
    return dec_to_bin (bres)

def increment(b):
    """ takes in binary string 'b' and returns 'b' incremented by one""" 
    if b == 11111111:
        return 00000000
    else:
        b = bin_to_dec(b)
        b = b + 1
        res = dec_to_bin (b)
        if len(res) == 8:
            return res
        else:
            c = 8 - len(res)
            return c*'0' + res 
    
