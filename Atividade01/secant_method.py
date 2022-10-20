def secant(func, x0, x1, n):
    def f(x):
        f = eval(func)
        return f

    print("k xk f(xk) stepk")

    counter = 1
    while counter <= n:
        fx0 = f(x0)
        fx1 = f(x1)
        xi = x0 - (fx0 / ((fx0-fx1) / (x0-x1)))
        print(f"{counter}|{fx0}|{fx1}|{x1}")
        x0 = x1
        x1 = xi
        counter = counter + 1

    print(f"Xi: {xi}")


secant("x**2-3", 1, 3, 5)
