# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:51:47 2020

@author: Carlos
"""

i=[1,2,3]
p=[7,6,5]
t=[30,20,10]
f = [7,13,18]
def photo(f,t):
    ans= ((f[2]-f[0]/t[0])+(f[1]-f[0]/t[1])+(0/t[2]))
    return ans

print(photo(f,t))