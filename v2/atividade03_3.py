import numpy as np

def criar_matriz_aumentada(matriz, vetor):
    n = matriz.shape[0]
    new_matrix = np.column_stack((matriz, vetor.reshape(n, 1)))
    print(new_matrix)
    return new_matrix

def gauss_jacobi(A_b, x):
    sum_j = 0
    for i in range(len(x)):
      for j in range(i + 1, len(x)):
          sum_j = sum_j + j
          A_b[j, :] = A_b[j, :] - (A_b[j, i] / A_b[i, i]) * A_b[i, :]
    print("iterações:" + str(sum_j))

    for i in reversed(range(len(x))):
        x[i] = (A_b[i, -1] - np.dot(A_b[i, i+1:len(x)], x[i+1:len(x)])) / A_b[i, i]


print("Atividade 3 - parte 1; Exercício 1:")
A = np.array([[1, -1, 0, 5],
              [3, -2, 1, -1],
              [1, 1, 9, 4],
              [1, -7, 2, 3]], dtype=float)
b = np.array([18, 8, 47, 32], dtype=float)
n = 4
x = np.zeros(n)
A_b = criar_matriz_aumentada(A, b)
gauss_jacobi(A_b, x)
print("Vetor solução x:"+ str(x) + "\n")

# Teste com outro exemplo
# A_2 = np.array([[10, 2,  1],
#      [ 1, 5,  1],
#      [ 2, 3, 10]], dtype=float)
# b_2 = np.array([7, -8, 6], dtype=float)
# n_2 = 3
# x_2 = np.zeros(n_2)
# A_b_2 = criar_matriz_aumentada(A_2, b_2)
# gauss_jacobi(A_b_2, x_2)
# print("Vetor solução x:", x_2)
