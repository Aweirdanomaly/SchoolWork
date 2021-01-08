# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:54:22 2020

@author: Carlos
"""

from itertools import combinations

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
ans = 0
for combo in combinations(lst, 3):  # 2 for pairs, 3 for triplets, etc
     if (combo[0] != combo[1] and combo[1] != combo[2] and combo[0] != combo[2]):
        # print (combo)
        ans +=1
        
print(ans)