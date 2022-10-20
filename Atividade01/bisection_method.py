def bisection(func, a, b, tolerance):
    def f(x):
        f = eval(func)
        return f

    current_error = abs(b-a)

    while current_error > tolerance:
        c = (b+a) / 2
        if f(a) * f(b) >= 0:
            print("Não existem raizes")
            quit()

        elif f(c)*f(a) < 0:
            b = c
            current_error = abs(b-a)

        elif f(c)*f(b) < 0:
            a = c
            current_error = abs(b-a)

    print(f"Erro atual: {current_error}")
    print(f"A: {a}")
    print(f"B: {b}")


bisection("(4*x**3) + 3*x-3", 0, 1, 0.05)
