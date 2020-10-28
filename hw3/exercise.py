'''
Siying homework3
'''
import timeit
import functools
import numpy as np

#1
def generate_s_matrix(size_of_matrix):
    '''Generates an NxN matrix where all edges are 1 and all inner values are 0.

    Parameters
    ----------
    size_of_matrix : int
        The size of the matrix.

    Returns
    -------
    s_matrix : Array
    Matrix with all edges of 1 and inner values of 0.

    '''
    s_matrix = np.ones((size_of_matrix,size_of_matrix))
    s_matrix[1:-1, 1:-1] = 0
    return s_matrix

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
    r_matrix : Matrix
        A rows x cols matrix with random number.

    '''
    r_matrix = np.random.random((rows, cols))
    r_matrix = np.matrix(r_matrix)
    return r_matrix

#3
def matrix_multiplication_loop(matrix_a,matrix_b):
    '''Multiplication of two matrices using for loop.
    Parameters
    ----------
    matrix_a : matrix
        X matrix.
    matrix_b : matrix
        Y matrix.

    Returns
    -------
    result : Array
        Final result of multiplication.

    '''
    row_x = len(matrix_a)
    col_y = len(matrix_b[0])
    row_y = len(matrix_b)
    result = [[0 for i in range(col_y)] for j in range(row_x)]
    # iterating by row of A
    for i in range(row_x):
        # iterating by coloum by B
        for j in range(col_y):
            # iterating by rows of B
            for k in range(row_y):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


#4
def timed_matrix_multiplication(matrix_a,matrix_b):
    '''
    Times how long it takes to multiply x and y(using loop).
    100X100 dot 100x100 matrix time: [1.6601724390000072]
    10x10   dot 10x10   matrix time: [0.0038878369999792994]
    '''
    t_used = timeit.timeit(functools.partial(matrix_multiplication_loop,matrix_a,matrix_b),\
            number =1)
    return t_used


#5
def matrix_multiplication_numpy(matrix_a,matrix_b):
    ''' Matrix multiplication by using numpy

    Parameters
    ----------
    matrix_a : matrix
        X matrix.
    matrix_b : matrix
        Y matrix.

    Returns
    -------
    Matirx
        Final reuslt of multiplication.

    '''
    return np.matrix(np.dot(matrix_a,matrix_b))

def timed_multiplication_numpy(matrix_a,matrix_b):
    '''
    Times how long it takes to multiply x and y(using numpy).
    100X100 dot 100x100 matrix time: [0.028776073000017277]
    10x10   dot 10x10   matrix time: [0.00027551499999844964]
    '''
    t_used = timeit.timeit(functools.partial(matrix_multiplication_numpy,matrix_a,matrix_b),\
            number = 1)
    return t_used
