# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:06:59 2019

@author: Carlos
"""

#Problem 7.1
def letter_score(letter):
    """ takes in string "letter" and returns how many scrabbles points you'd get"""
    if len(letter) == 1 and letter in ['m', 'a', 'n', 'o', 'r', 'e', 's', 't', 'u', 'i', 'l', 'g', 'd', 'b', 'c', 'p', 'f' , 'h' , 'v' , 'w' , 'y', 'k', 'j' , 'x','q' , 'z']:
       if  letter in ['a', 'n', 'o', 'r', 'e', 's', 't', 'u', 'i', 'l' ]:
                return 1
       elif letter in ['g', 'd']:
                return 2
       elif letter in ['b', 'c', 'p', 'm']:
                return 3
       elif letter in ['f' , 'h' , 'v' , 'w' , 'y']:
                return 4
       elif letter in ['k']:
                return 5
       elif letter in ['j' , 'x']:
                return 8
       elif letter in ['q' , 'z']:
                return 10
    else:
        return 0
    
#problem 7.2
def scrabble_score(word):
    """ takes in string "word" and calculates amount of scrable
    points that it can get you by calling letter_score"""
    if (word) == '':
        return 0
    else:
        b = scrabble_score(word[1:])
        b = b + letter_score(word[0])
        return b
    
    
#problem 7.3 
def add(vals1, vals2):
    """ takes two lists 'vals1' and 'vals2' as inputs
    and outputs a list of their combined scrabble values"""
    if (vals1) == []:
        return []
    else:
        b = add(vals1[1:], vals2[1:])
        
        return ( [vals1[0] + vals2[0]] + b)

#problem 7.4
def weave(s1, s2):
    """ takes in 2 strings "s1" and "s2" and returns
    string alternating between their elements"""
    if len(s1) == 0 and len(s2) == 0:
        return ''
    elif len(s2) == 0:
        return s1
    elif len(s1) == 0:
        return s2
        
    else:
        b = weave(s1[1:],s2[1:])
        
        return  s1[0] + s2[0] + b
        
                     
        
        
        
        
        
        
        
    
    
              
            
        
    