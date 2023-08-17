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


def sqrt(A):
  x = A
  while x**2 - A > 0.00000001:
    x = (x + A/x) / 2
  return x

# Aquecimento
print(bisection("(x/(x**2 + 1)**(3/2)) -0.1668", 0, 1, 0.00000001))

# Atividade 1 - 1
print(bisection("(x**2)-2", 0, 2, 0.00000001))

## Atividade 1 - 2
print(sqrt(2))