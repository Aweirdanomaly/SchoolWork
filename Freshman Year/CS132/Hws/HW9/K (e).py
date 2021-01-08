# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 03:06:45 2020

@author: Carlos
"""
from math import *
import numpy as np


def ProblemK (f):
    v1=np.array([[((1+sqrt(5))/2),1]])
    v2=np.array([[((1-sqrt(5))/2),1]])
    x=(.28)*pow(((1+sqrt(5))/2), f)
    y=(.72)*pow(((1-sqrt(5))/2),f)
    answer=x*v1+y*v2
    return answer

def ProblemL (k):
    v2=np.array([.097,-.561,-.106,.040,-.813,-.285])
    x=(-.13)*pow(1.034, k)
    answer = x*v2
    return answer
    