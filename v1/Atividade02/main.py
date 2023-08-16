import numpy as np
from gauss_jacobi import run as gJacobi
from gauss_jacobi import plot as gJacobiPlot
from gauss_seidel import run as gSeidel
from tabulate import tabulate

# Questao 2


def generate_matrix(alpha, beta, n):
    matrix = [[0]*n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if (j == i):
                matrix[i][j] = alpha
            elif (j == i-1 or j == i+1):
                matrix[i][j] = -1*beta
            else:
                matrix[i][j] = 0
    return np.array(matrix)

# Questao 2


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
x_array = [0 for i in range(len(b_array))]

print(A_matrix)
print(b_array)
print(x_array)

# A = [[3, -1,  1],
#      [1, 5,  -2],
#      [2, -1, 4]]

# b = [3, 4, 5]

# Questao 3

x = gJacobi(A_matrix, b_array, x_array, 2000, 0.00000001, True)
print("x = ", x)

x = gSeidel(A_matrix, b_array, x_array, 2000, 0.00000001, True)
print("x = ", x)


# Questão 4
number_of_iterations = list(range(1, 11))
saida = []
for i in number_of_iterations:
    A_matrix = generate_matrix(i, 2, 20)
    b_array = generate_array_b(i, 2, 20)
    x, jacobi_iterations = gJacobi(
        A_matrix, b_array, x_array, 2000, 0.00000001, False)
    x, seidel_iterations = gSeidel(
        A_matrix, b_array, x_array, 2000, 0.00000001, False)
    saida.append([i, jacobi_iterations, seidel_iterations])

print(tabulate(saida, headers=["alpha", "Jacobi", "Seidel"]))
