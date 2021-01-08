# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:11:35 2020

@author: Carlos
"""

import numpy as np

# Part A
alpha = .01
P1 = np.array([[0,0,1,0,0],[1/3,0,0,1/2,0],[1/3,0,0,1/2,0],[1/3,1/2,0,0,0],[0,1/2,0,0,0]])
P2 = np.array([[0,1/2,1/4,0,0,0],[0,0,1/4,0,0,0],[0,1/2,0,1/2,0,0],[0,0,1/4,0,1/2,0],[0,0,1/4,1/2,0,0],[0,0,0,0,1/2,0]])
print('\n' "Here's the transition matrix for I-1:""\n" , P1)
print('\n' "Here's the transition matrix for I-2:""\n", P2)



#Part B
P1p = np.array([[0,0,1,0,1/5],[1/3,0,0,1/2,1/5],[1/3,0,0,1/2,1/5],[1/3,1/2,0,0,1/5],[0,1/2,0,0,1/5]])
P2p = np.array([[0,1/2,1/4,0,0,1/6],[0,0,1/4,0,0,1/6],[0,1/2,0,1/2,0,1/6],[0,0,1/4,0,1/2,1/6],[0,0,1/4,1/2,0,1/6],[0,0,0,0,1/2,1/6]])
FP1 = ((1-alpha)*P1p + (alpha/5))
FP2 = ((1-alpha)*P2p + (alpha/6)) 
print('\n' "Here's the P'' for I-1:""\n", FP1)
print('\n' "Here's the P'' for I-2:""\n", FP2)


#Part C
def PartC(graph, x):
    eigenvalues, eigenvectors = np.linalg.eig(x)
    MaxVal = np.argmax(eigenvalues)
    print("\n" "Here's the steady-state vector for I-",graph, ": ""\n", eigenvectors[MaxVal])
    return eigenvectors[MaxVal]
Vector1 = PartC("1", FP1)
Vector2 = PartC("2", FP2)

#Part D
def PartD(graph, x):
    #Note that this is sorted from least to greatest (backwards)
    reverseOrder = np.argsort(x)
    ActualAnswer = 1 + reverseOrder[::-1]
    print("\n""The order in which the pages for I-",graph, " would be presented would be: ", ActualAnswer)
    print()

PartD("1", Vector1)
PartD("2", Vector2)
