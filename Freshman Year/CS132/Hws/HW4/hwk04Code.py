import numpy as np

def innerProduct(a,b):
    """
    Takes two vectors a and b, of equal length, and returns their inner product
    """
    sum = 0
    for x in range(len(a)):
        sum += a[x] * b[x]
    return sum
    
def AxIP(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    p = np.zeros(A.shape[0]) #make a zero array of the length of rows in matrix A
    for w in range(len(A)):
        p[w] = innerProduct(A[w,:], x) #fill empty array with the resulting vector b
    return p

def AxVS(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    ans = np.zeros(A[:,0].shape) # make zero array of length of rows in matrix A
    for w in range(len(A[0])):
       ans += x[w] * A[:, w]# fill empty array with sum of vector x and every column in matrix A
    return ans
        
        
