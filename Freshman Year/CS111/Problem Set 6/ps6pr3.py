# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:31:41 2019

@author: Carlos
"""

def double(s):
    """ takes in string 's' and returns 's' with each of its
    characters doubled"""
    result = ''

    for c in s:
       result +=(c* 2)
    return result
       
def weave(s1, s2):
    """ takes in two strings 's1' and 's2' and returns a single string
    composed of the characters in 's1' and 's2' interweaved"""
    result = ''
    len_shorter = min(len(s1), len(s2))

    for i in range(len_shorter):
        result += s1[i]
        result += s2[i]
    i += 1
    if len(s1) > len(s2):
        result += s1[i:]
    elif len(s2) > len(s1):
        result += s2[i:] 
    return result
    
def index(elem, seq):
    """takes in string or list 'seq' and int or string 'elem' and returns
    the position in which the first instance of 'elem' is found in 'seq' """

    for i in range(len(seq)):
        if seq[i] == elem:
            break
        elif i == (len(seq)) - 1:
            return -1
    return i
        