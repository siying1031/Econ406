"""
Siying homework3 Q2
"""
import pandas as pd
import numpy as np

#1
def generate_s_matrix(n): 
    '''Generates an NxN matrix where all edges are 1 and all inner values are 0.    

    Parameters
    ----------
    n : int
        The size of the matrix.

    Returns
    -------
    z : Array
    Matrix with all edges of 1 and inner values of 0.  

    '''
    z = np.ones((n,n))
    z[1:-1, 1:-1] = 0
    return z

#2
def generate_matrix(rows, cols):
    ''' Generate a rows x cols matrix with random number.
 
    Parameters
    ----------
    rows : Int
        number of rows.
    cols : Int
        number of columns.

    Returns
    -------
    z : Matrix
        A rows x cols matrix with random number.

    '''
    z = np.random.random((rows, cols))
    z = np.matrix(z)
    return z

#3
def matrix_multiplication_loop(x,y):
    '''Multiplication of two matrices using for loop.
    

    Parameters
    ----------
    x : Matrix
        X matrix.
    y : Matrix
        Y matrix.

    Returns
    -------
    result : Array
        Final result of multiplication.

    '''
    row_x = len(x)
    col_y = len(y[0])
    row_y = len(y)
    result = [[0 for i in range(col_y)] for j in range(row_x)]
    # iterating by row of A 
    for i in range(row_x): 
        # iterating by coloum by B  
        for j in range(col_y): 
            # iterating by rows of B 
            for k in range(row_y):
                result[i][j] += x[i][k] * y[k][j]
    return result
                 
    
#4
def timed_matrix_multiplication(x,y):
    '''
    Times how long it takes to multiply x and y(using loop).
    100X100 dot 100x100 matrix time: [1.6601724390000072]
    10x10   dot 10x10   matrix time: [0.0038878369999792994]
    '''
    t = timeit.timeit(functools.partial(matrix_multiplication_loop,x,y),number =1)
    return t


#5
def matrix_multiplication_numpy(x,y):
    ''' Matrix multiplication by using numpy
    
    Parameters
    ----------
    x : Matrix
        X matrix.
    y : Matrix
        Y matrix.

    Returns
    -------
    Matirx
        Final reuslt of multiplication.

    '''
    return np.matrix(np.dot(x,y))

def timed_multiplication_numpy(x,y):
    '''
    Times how long it takes to multiply x and y(using numpy).
    100X100 dot 100x100 matrix time: [0.028776073000017277]
    10x10   dot 10x10   matrix time: [0.00027551499999844964]
    '''
    t = timeit.timeit(functools.partial(matrix_multiplication_numpy,x,y),number = 1)
    return t

                