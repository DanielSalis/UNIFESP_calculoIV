import numpy as np
from gauss_jacobi import run as gJacobi
from gauss_seidel import run as gSeidel


def generate_matrix(alpha, beta, n):
    matrix = [[0]*n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if (j == i):
                matrix[i][j] = alpha
            elif (j == i-1 or j == i+1):
                matrix[i][j] = beta
            else:
                matrix[i][j] = 0
    return np.array(matrix)


def generate_array_b(alpha, beta, n):
    array = [0 for i in range(n)]
    for j in range(0, n):
        if (j == 0 or j == n-1):
            array[j] = alpha - beta
        else:
            array[j] = alpha-(2*beta)
    return array


A_matrix = generate_matrix(4, 1, 20)
b_array = generate_array_b(4, 1, 20)

print(A_matrix)
print(b_array)

A = [[10, 2,  1],
     [1, 5,  1],
     [2, 3, 10]]

b = [7, -8, 6]

x = gJacobi(A, b, 10, 0.01)
print("x = ", x)

x = gSeidel(A, b, 10, 0.01)
print("x = ", x)
