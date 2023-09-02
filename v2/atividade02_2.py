from tabulate import tabulate
import numpy as np
import math

def cps_equation(A):
    h = 290
    C = 1100
    F = 0.7
    D = 13

    numerador = math.pi * (h / math.cos(A)) ** 2 * F
    denominador = 0.5 * math.pi * D ** 2 * (1 + math.sin(A) - 0.5 * math.cos(A))

    return C - numerador / denominador

def cps_derivate(A):
    h = 290
    F = 0.7
    D = 13

    numerador = -2 * math.pi * h ** 2 * F * math.tan(A) / math.cos(A) ** 3
    denominador = 0.5 * math.pi * D ** 2 * (math.cos(A) + 0.5 * math.sin(A))

    return numerador / denominador

def oxygen_equation(x):
    return 10 - 20 * ((np.exp(-0.2*x)) - (np.exp(0.75*x))) - 5

def equacao_colebrook_1(f):
    Re = 3*(10e5),
    epsilon_DH = 0.0001
    return 1 / (math.sqrt(f)) + 2 * math.log10(epsilon_DH / 3.7 + 2.51 / (Re[0] * math.sqrt(f)))

def bisectionMehod(func, a, b, tolerance=1e-6):
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

    return c

def newtonsMethod(func, der, x0, tolerance=1e-6, max_iter=100):
    x = x0
    iteracao = 0

    while iteracao < max_iter:
        delta_x = func(x) / der(x)
        x = x - delta_x

        if abs(delta_x) < tolerance:
            return x

        iteracao += 1

    return None

def secantMethod(func, x0, x1, tolerance, max_iteractions):
    saida = []
    for iteraction in range(1, max_iteractions, 1):
        fx0 = func(x0)
        fx1 = func(x1)
        if abs(fx1) < tolerance:
            return xi
            break
        xi = x1 - fx1*((x1-x0)/(fx1-fx0))
        fxi = func(xi)
        saida.append([iteraction, xi, fxi, fx0])
        x0 = x1
        x1 = xi

    # return tabulate(saida, headers=["iteraction", "xi", "func(xi)", "fx0"])

    h = 290
    F = 0.7
    D = 13

    numerador = -2 * math.pi * h ** 2 * F * math.tan(A) / math.cos(A) ** 3
    denominador = 0.5 * math.pi * D ** 2 * (math.cos(A) + 0.5 * math.sin(A))

    return numerador / denominador

print("\nAtividade 2_2 - 1")
print("Utilizando o método de newton conseguimos encontrar o valor: " + str(newtonsMethod(cps_equation, cps_derivate, 1, 1e-6, 100)))

print("\nAtividade 2_2 - 2")
print("Utilizando o método de newton conseguimos encontrar o valor: " + str(secantMethod(oxygen_equation, -1, 1, 1e-6, 100)))


casos = [
    {"Re": 3e5, "epsilon_DH": 0.0001},
    {"Re": 1e4, "epsilon_DH": 0.03},
    {"Re": 3e5, "epsilon_DH": 0.01}
]
print("\nAtividade 2_2 - 3")
print("Utilizando o método da secante conseguimos encontrar o valor: " + str(secantMethod(equacao_colebrook_1, 0.0001, 0.0003, 1e-6, 100)))
print("Utilizando o método da bissecção conseguimos encontrar o valor: " + str(bisectionMehod(equacao_colebrook_1, 0.0001, 1, 1e-6)))