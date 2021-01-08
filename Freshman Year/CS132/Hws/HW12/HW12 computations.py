# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:04:19 2020

@author: Carlos
"""

import numpy as np

def ProblemSolver(X,y):
    print("\n Here's what X looks like:\n", X)
    print("\n Here's what y looks like:\n", y)
    Beta = (np.linalg.inv(X.transpose()@X))@(X.transpose()@y) #(X^T*X)^-1(X^T*y)
    print("\n Here's what Beta looks like:\n", Beta)
    
def ProblemK():
    X=np.array([[4,16,64],[6,36,216],[8,64,512],[10,100,1000],[12,144,1728]
                ,[14,196,2744],[16,256,4096],[18,324,5832]])
    y=np.array([[1.58],[2.08], [2.5], [2.8], [3.1], [3.4],[3.8],[4.32]])
    ProblemSolver(X,y)
    
def ProblemL():
    
    X=np.array([[np.e**(-.02*(10)),np.e**(-.07*(10))],
                [np.e**(-.02*(11)),np.e**(-.07*(11))],
                [np.e**(-.02*(12)),np.e**(-.07*(12))],
                [np.e**(-.02*(14)),np.e**(-.07*(14))],
                [np.e**(-.02*(15)),np.e**(-.07*(15))]])
    y=np.array([[21.34],[20.68],[20.05],[18.87],[18.30]])
    ProblemSolver(X,y)
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    