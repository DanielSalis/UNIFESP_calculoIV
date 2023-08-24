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

def newtonsMethod(function_statement, derivative_statement, x, n):
    iteration = 0
    saida = []

    def function(x):
        f = eval(function_statement)
        return f

    def derivative(x):
        d = eval(derivative_statement)
        return d

    while abs(function(x)) >= 0.000001 and iteration <= n:
        saida.append([iteration,x,function(x)])
        i = x - (function(x) / derivative(x))
        x = i
        iteration += 1

    return tabulate(saida, headers=["iteration", "x", "f(x)"])

# print(newtonsMethod("x**2 - 2 ", "2*x", 2, 10) + '\n')
print(newtonsMethod("x**3 - x**2 - 1 ", "3*x**2 - 2*x", 2, 10) + '\n')
print(bisection("x**3 - x**2 - 1 ", 0, 2, 0.000001) + '\n')
print("Podemos perceber que o método da bissecção demorou 20 iterações enquanto o de newton apenas 4")
