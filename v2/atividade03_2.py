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
n2 = 3
A2 = np.array([[1, 1, 1],
               [1, 1, 2],
               [2, 3, 5]], dtype=int)

b2 = np.array([400, 600, 1500], dtype=int)
x2 = np.zeros(n2)
A_b2 = criar_matriz_aumentada(A2, b2)
gauss_jacobi(A_b2, x2)
print("Não foi possível a conversão\nDevido ao fato de que a matriz A2 não atende aos critérios de diagonal estritamente dominante ou diagonal dominante em todas as linhas, não podemos garantir a convergência do método de Gauss-Jacobi para este sistema.")
# Para a primeira linha: 1 > 1 + 1 (não é estritamente dominante).
# Para a segunda linha: 1 > 1 + 2 (não é estritamente dominante).
# Para a terceira linha: 5 > 2 + 3 (é estritamente dominante).