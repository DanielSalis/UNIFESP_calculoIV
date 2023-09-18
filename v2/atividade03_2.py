import numpy as np
import matplotlib.pyplot as plt

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



print("Atividade 3 - parte 2; Exercício 1:")
n2 = 3
A2 = np.array([[70, 20, 10],
               [10, 90, 0],
               [15, 10, 75]], dtype=int)

b2 = np.array([4000, 1000, 2000], dtype=int)
x2 = np.zeros(n2)
A_b2 = criar_matriz_aumentada(A2, b2)
gauss_jacobi(A_b2, x2)
print("Vetor solução x:"+ str(x2) + "\n")

print("Atividade 3 - parte 2; Exercício 3:")
# Given data
T = np.array([0, 5, 10, 15, 20, 25])
C = np.array([14.5, 12.6, 11.3, 10.3, 9.1, 8.5])

plt.scatter(T, C, label='Data Points', color='black')
plt.title('Plot dos pontos')
plt.xlabel('T')
plt.ylabel('C')
plt.show()

# Método de newton
def divided_difference(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])

    return F

# Coefficients of the interpolation polynomial
coefficients = divided_difference(T, C)[0]

# Function to evaluate the interpolation polynomial
def interpolate(x, coefficients, T):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        term = coefficients[i]
        for j in range(i):
            term *= (x - T[j])
        result += term
    return result

# Generate points on the interpolation polynomial
x_values = np.linspace(0, 25, 100)
y_values = [interpolate(x, coefficients, T) for x in x_values]

# Plot the given data points
plt.scatter(T, C, label='Data Points', color='red')

# Plot the interpolation polynomial
plt.plot(x_values, y_values, label='Interpolation Polynomial', color='blue')

plt.xlabel('T')
plt.ylabel('C')
plt.legend()
plt.title('Interpolação com método de newton')
plt.grid(True)
plt.show()