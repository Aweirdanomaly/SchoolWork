from collections import deque
import random

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:58:02 2020

@author: Carlos
"""




def m():
    H=deque()
    Q = []
    H.extend(('0','1','2','3','4'))
    ye = H[0]
    H.popleft()
    print(ye , H)
    print('q', Q)
    
print(random.uniform(0,1))