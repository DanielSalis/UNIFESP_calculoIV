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


def heron(n, a_initial):
    i = 0
    prev = a_initial
    saida = []
    error = 1
    while error >= 0.000001:
        new = 0.5 * (prev + n/prev)
        error = abs(new - prev)
        prev = new
        i = i + 1
        saida.append([i, new, error])

    return tabulate(saida, headers=["iteration", "a_current", "error"])

print('Aquecimento')
print(bisection("(x/(x**2 + 1)**(3/2)) -0.1668", 0, 1, 0.000001))
print('\n')

print('Atividade 1 - 1')
print(bisection("(x**2)-2", 0, 2, 0.000001))
print('\n')

print('Atividade 1 - 2')
print(heron(2, 1))
print('\n')

print('Atividade 1 - 3')
print(heron(2, 2))
print('\n')

print('Atividade 1 - 4')
print('Erros já estão sendo calculados\n')