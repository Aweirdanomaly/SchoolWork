# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:49:01 2019

@author: Carlos
"""


"""  rots_list = [[x] for x in rots]
rots_elem = [x for x in rots_list]
final = [[x for y in rots_elem for x in y] ]
final2 = [[x for y in final for x in y] ]"""

s= [2,5,7]
import random
import numpy as np

def count_ones(s):
    return len([x for x in s if x == '1'])

def swap_bits(s):
    if s == '':
        return ''
    else:
        b = swap_bits(s[1:])
        if s[0] == '0':
            return '1' + b
        else:
            return '0' + b
            
        
def num_divisors(n):
    return len([x for x in range(1, n+1) if n % x ==0])

def most_divisors(lst):
    b = max([[num_divisors(x), x] for x in lst])
    return b[1]

def F(n, m):
    if m == 0:
        return 1
    elif m != 0 and m % 2 == 0:
        b =F(n, m/2)
        return b**2
    elif m !=0 and m%2 == 1:
        c =F(n, m-1)
        return c *n

#
def v(s):
    """ counts vowels in input string 's' """
    count = 0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            count += 1
    return count
    
def years_needed(principal, rate, target):
    count = 0
    while principal < target:    
        principal = principal * (1 + rate)
        count += 1
    return count
def stars(n):
    i = 0
    while i < n+1:
        for x in range(i):
            print('*', end= '')
        print()
        i += 1
        
def all_perfect(lst):
    for i in range(len(lst)):
        if lst[i] != 100:
            return False
        
    return True

def index_nearest(n, lst):
    ans = 0
    for x in range(len(lst)):
        if abs(lst[x]-n) < abs(lst[ans]-n):
            ans = x
    return ans



def index():
    lst = [[1, 2], [3, 4], [5, 6]]

    for idx, b in lst:  

        print (idx, b)


def matrix_bois():
    A = np.random.randint(6, size=(4,4))
    # I = np.identity(4)
    # difference = (A+I)@(A-I)-((A@A)-I)
    # print(difference)
    B = np.random.randint(6, size=(4,4))
    difference2 = (A+B)@(A-B)-((A@A)-(B@B))
    print(difference2)






