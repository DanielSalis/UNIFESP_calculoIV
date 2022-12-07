from gauss_jacobi import run as gJacobi
from gauss_seidel import run as gSeidel

A = [[10, 2,  1],
     [1, 5,  1],
     [2, 3, 10]]

b = [7, -8, 6]

x = gJacobi(A, b, 10, 0.01)
print("x = ", x)

x = gSeidel(A, b, 10, 0.01)
print("x = ", x)
