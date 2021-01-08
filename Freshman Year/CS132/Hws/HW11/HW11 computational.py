# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 04:42:24 2020

@author: Carlos
"""

import numpy as np

def problemO():
    A= np.array([[-6,-3,6,1],[-1,2,1,-6],[3,6,3,-2],[6,-3,6,-1],[2,-1,2,3],[-3,6,3,2],[-2,-1,2,-3],[1,2,1,6]])
    print("Here's the original matrix:\n",A,"\n")
    At= A.transpose()
    print("Here's the transposed matrix:\n",At,"\n")
    Answer = At.dot(A)
    print("Heree's the transposed matrix times the original matrix:\n",Answer)
    print("\nSince every entry that's not on the diagonal is zero, the columns of the original matrix are orthogonal")