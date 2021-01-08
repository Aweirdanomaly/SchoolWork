# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 02:42:17 2019

@author: Carlos
"""

def bitwise_and(b1, b2):
    """ takes in binary strings 'b1' and 'b2' and returns their bitwise AND"""
    if b1 == '' and b2 == '':
        return ''
    elif b1 != '' and b2 == '':
        return (len(b1) * '0')
    elif b1 == '' and b2 != '':
        return (len(b2) * '0')
    else:
        b = bitwise_and(b1[0:-1], b2[0:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return b + '1' 
        else:
            return b + '0'

def add_bitwise(b1, b2):
    """ adds two binary strings 'b1' and 'b2' through elementary approach
    and returns their resulting binary string"""
    if b1 == '' and b2 == '':
        return ''
    elif b1 != '' and b2 == '':
        return b1
    elif b1 == '' and b2 != '':
        return b2
    else:
        b = add_bitwise(b1[0:-1], b2[0:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return b + '0'
        elif b1[-1] == '1' and b2[-1] == '1':
            b = b + '0'
            c = add_bitwise(b, '10')
            return  c 
        elif b1[-1] == '1' or b2[-1] == '1': 
            return b + '1'
 
    