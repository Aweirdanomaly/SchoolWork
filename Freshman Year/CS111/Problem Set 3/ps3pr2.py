# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:20:06 2019

@author: Carlos
"""

#Problem 2.1
def cube_all_lc(values):
    """takes in list of values 'values' and returns the same list but with
    its own elements cubed through list comprehension"""
    return [x*x*x for x in values]

#Problem 2.2
def cube_all_rec(values):
    """takes in list of values 'values' and returns the same list but with
    its own elements cubed through recursion"""
    if values == []:
        return []
    else:
        b = cube_all_rec(values[1:])
        return [(values[0]*values[0]*values[0])] + b
    
#Problem 2.3
def num_larger(threshold, values):
    """takes in int 'threshold' and list 'values' and returns amount of
    numbers in 'values' bigger than 'threshold' """
    return len([x for x in values if x > threshold])

#helper function for 2.4
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

#Problem 2.4
def most_consonants(words):
    """takes in list of strings 'words' and returns the string in that list
    with the most consonants"""
    a = max([[(len(x) - num_vowels(x)) , x] for x in words])  
    return a[1]    
 
#Problem 2.5
def price_string(cents):
    """takes in an int 'cents' and returns a string expressing the monetary
    value in dollars and cents"""
    d = cents // 100  # compute whole number of dollars
    c = cents % 100   # compute remaining cents

    price = ''            # initial value of the price string

    ## add code below to build up the price string
    if d == 0:
        price = price
    elif d == 1:
        price = str(d) + ' dollar'
    else:
        price = str(d) + ' dollars'
    if d != 0 and c != 0:
        price = price + ', '
    if c == 0:
        price = price 
    elif c == 1:
        price = price + str(c) + ' cent'
    else:
        price = price + str(c) + ' cents'

    return price


