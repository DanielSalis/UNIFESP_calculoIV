from tabulate import tabulate


def secant(func, x0, x1, n):
    def f(x):
        f = eval(func)
        return f

    counter = 1
    k = 0
    saida = []
    while k <= n:
        fx0 = f(x0)
        fx1 = f(x1)
        xi = x0 - (fx0 / ((fx0-fx1) / (x0-x1)))
        fxi = f(xi)
        x0 = x1
        x1 = xi
        k = k + 1
        saida.append([k, xi, fxi, fx0])

    return tabulate(saida, headers=["k", "xk", "f(xk)", 'stepk'])


print(secant("x**2-2", 1, 2, 5))
