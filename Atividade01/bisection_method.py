from tabulate import tabulate


def bisection(func, a, b, tolerance):
    def f(x):
        f = eval(func)
        return f

    current_error = abs(b-a)
    k = 0
    saida = []
    fk = 0
    while current_error > tolerance:
        c = (b+a) / 2
        if f(a) * f(b) >= 0:
            print("Não existem raizes")
            quit()

        elif f(c)*f(a) < 0:
            b = c
            current_error = abs(b-a)
            fk = f(c)*f(a)

        elif f(c)*f(b) < 0:
            a = c
            current_error = abs(b-a)
            fk = f(c)*f(b)

        k += 1
        saida.append([k, c, fk, current_error])

    return tabulate(saida, headers=["k", "xk", "f(xk)", 'stepk'])


# print(bisection("(4*x**3) + 3*x-3", 0, 1, 0.05))
print(bisection("(x/(x**2 + 1)**(3/2)) -0.1668", 0, 1, 0.00000001))
