# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:24:49 2019

@author: Carlos
"""

def index(elem, seq):
    """ takes in list element or string element 'elem' and full list or full
    string 'seq' and outputs the first position in which 'elem' is in 'seq' """
    if seq == '' or seq == []:
        return -1
    elif seq[0] == elem:
        return 0 #len(seq) - 1
   
    else:
        b = index(elem, seq[1:])
        if b == -1:
            return b
        else:
            return b + 1
       
def index_last(elem, seq):
    """ takes in list element or string element 'elem' and full list or full
    string 'seq' and outputs the last position in which 'elem' is in 'seq' """
    if seq == '' or seq == []:
       return -1
    elif seq[-1] == elem:
       return len(seq) - 1
   
    else:
        b = index_last(elem, seq[0:-1])
        if b == -1:
            return b
        else:
            return b 
         
            
def jscore(s1, s2):
    """ takes in two strings 's1' and 's2' and returns their Jotto score
    """
    if s1 == '' or s2 == '':
        return 0
    else:
        b = jscore(s1[0:-1], s2)
        if s1[-1] in s1[0:-1]:
            s2 = rem_first(s1[-1], s2)
            if s1[-1] in s2:
                return b + 1
            else:
                return b
                
            return b
        elif s1[-1] in s2:
            s2 = rem_first(s1[-1], s2)
            return  b + 1
        else: 
            return b
    
def rem_first(elem, values):
    """ removes the first occurrence of elem from the string values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest
    
    