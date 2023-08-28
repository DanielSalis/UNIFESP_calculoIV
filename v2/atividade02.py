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

def newtonsMethod(function_statement, derivative_statement, x, max_iteractions):
    iteration = 0
    saida = []

    def function(x):
        f = eval(function_statement)
        return f

    def derivative(x):
        d = eval(derivative_statement)
        return d

    while abs(function(x)) >= 0.000001 and iteration <= max_iteractions:
        saida.append([iteration,x,function(x)])
        i = x - (function(x) / derivative(x))
        x = i
        iteration += 1

    return tabulate(saida, headers=["iteration", "x", "f(x)"])

def secantMethod(func, x0, x1, tolerance, max_iteractions):
    def f(x):
        f = eval(func)
        return f

    saida = []
    for iteraction in range(1, max_iteractions, 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tolerance:
            break
        xi = x1 - fx1*((x1-x0)/(fx1-fx0))
        fxi = f(xi)
        saida.append([iteraction, xi, fxi, fx0])
        x0 = x1
        x1 = xi

    return tabulate(saida, headers=["iteraction", "xi", "f(xi)", "fx0"])

# print(newtonsMethod("x**2 - 2 ", "2*x", 2, 10) + '\n')
print(newtonsMethod("x**3 - x**2 - 1 ", "3*x**2 - 2*x", 2, 10) + '\n')
print(bisection("x**3 - x**2 - 1 ", 0, 2, 0.000001) + '\n')
print("Podemos perceber que o método da bissecção demorou 20 iterações enquanto o de newton apenas 4")

print("\nAtividade 2 - 2")
print("\nBisecção\n", bisection("x**2 - 7", 1, 3, 0.000001))
print("\nNewton\n", newtonsMethod("x**2 - 7", "2*x", 7, 100))
print("\nSecante\n", secantMethod("x**2 - 7", 1, 3, 0.000001, 100))
print("Podemos perceber que o método da secante demorou 4 iterações, o de newton também 4 e o da bissecção demorou 20")

print("\nAtividade 2 - 3")