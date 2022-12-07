from gauss_jacobi import run as gJacobi

A = [[10, 2,  1],
     [1, 5,  1],
     [2, 3, 10]]

b = [7, -8, 6]

x = gJacobi(A, b, 1000, 0.0001)
print("x = ", x)
