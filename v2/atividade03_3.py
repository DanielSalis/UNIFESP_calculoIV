import numpy as np

def gauss_jacobi(A, b, tol=1e-6, max_iter=50):
    n = len(b)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iterations = 0

    while iterations < max_iter:
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        print(x_new)

        if np.all(np.abs(x_new - x) < tol):
            return x_new  # Retorna o vetor solução se convergir

        x = x_new.copy()
        iterations += 1

    print("O método não convergiu após {} iterações.".format(max_iter))
    return None

# Exemplo de uso:

A_matrix = np.array([[1, -1, 0, 5],
                     [3, -2, 1, -1],
                     [1, 1, 9, 4],
                     [1,-7,2,3]])
b_array = np.array([18,8,47,32])
x_array = [0 for i in range(len(b_array))]

solucao = gauss_jacobi(A_matrix, b_array)

if solucao is not None:
    print("A solução do sistema é:")
    print(solucao)
