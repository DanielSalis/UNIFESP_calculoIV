from tabulate import tabulate
import numpy as np

def bisection(func, a, b, tolerance):
    current_error = abs(b-a)
    k = 1
    saida = []
    fk = 0
    while current_error >= tolerance:
        c = (b+a) / 2
        if func(a) * func(b) >= 0:
            print("Não existem raizes")
            quit()

        elif func(c)*func(a) < 0:
            b = c
            current_error = abs(b-a)
            fk = func(c)*func(a)

        elif func(c)*func(b) < 0:
            a = c
            current_error = abs(b-a)
            fk = func(c)*func(b)

        saida.append([k, c, fk, current_error])
        k += 1

    return tabulate(saida, headers=["k", "xk", "f(xk)", 'error'])

def newtonsMethod(function_statement, derivative_statement, x, max_iteractions):
    iteration = 1
    saida = []

    def function(x):
        f = eval(function_statement)
        return f

    def derivative(x):
        d = eval(derivative_statement)
        return d

    while abs(function(x)) >= 1e-6 and iteration <= max_iteractions:
        saida.append([iteration,x,function(x)])
        i = x - (function(x) / derivative(x))
        x = i
        iteration += 1

    return tabulate(saida, headers=["iteration", "x", "f(x)"])

def secantMethod(func, x0, x1, tolerance, max_iteractions):
    saida = []
    for iteraction in range(1, max_iteractions, 1):
        fx0 = func(x0)
        fx1 = func(x1)
        if abs(fx1) < tolerance:
            break
        xi = x1 - fx1*((x1-x0)/(fx1-fx0))
        fxi = func(xi)
        saida.append([iteraction, xi, fxi, fx0])
        x0 = x1
        x1 = xi

    return tabulate(saida, headers=["iteraction", "xi", "func(xi)", "fx0"])

print("\nAtividade 2 - 1")
def equation(x):
    return x**3 - x**2 - 1
print(newtonsMethod("x**3 - x**2 - 1 ", "3*x**2 - 2*x", 2, 10) + '\n')
print(bisection(equation, 0, 2, 1e-6) + '\n')
print("Podemos perceber que o método da bissecção demorou 20 iterações enquanto o de newton apenas 4")

print("\nAtividade 2 - 2")
def equationI(x):
    return x**2 - 7
print("\nBisecção\n", bisection(equationI, 1, 3, 1e-6))
print("\nNewton\n", newtonsMethod("x**2 - 7", "2*x", 7, 100))
print("\nSecante\n", secantMethod(equationI, 1, 3, 1e-6, 100))
print("Podemos perceber que o método da secante demorou 4 iterações, o de newton 5 e o da bissecção demorou 20")


print("\nAtividade 2 - 3")
def equationII(t, k = 0.67):
    return np.exp(-0.5 * t) * np.arccosh(np.exp(0.5 * t)) - np.sqrt(k / 2)

print("\nBisecção\n", bisection(equationII, 1, 3, 1e-6))
print("\nSecante\n", secantMethod(equationII, 1, 3, 1e-6, 100))
print("Podemos perceber que o método da secante demorou 4 iterações, bissecção demorou 20")
