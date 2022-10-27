from tabulate import tabulate


def secant(func, x0, x1, tolerance, num_inter):
    def f(x):
        f = eval(func)
        return f

    saida = []
    for k in range(1, num_inter, 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 < tolerance):
            break
        xi = x1 - fx1*((x1-x0) / (fx1-fx0))
        fxi = f(x0)
        saida.append([k, xi, fxi, fx0])
        x0 = x1
        x1 = xi

    return tabulate(saida, headers=["k", "xk", "f(xk)", 'stepk'])


print(secant("(x/(x**2 + 1)**(3/2)) - 0.1668", 0.3, 0.6, 0.000000000001, 20))
