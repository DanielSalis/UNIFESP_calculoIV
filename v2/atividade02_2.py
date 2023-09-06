from tabulate import tabulate
import numpy as np
import math
import matplotlib.pyplot as plt


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
    Re = 3*(10e4),
    epsilon_DH = 0.0001
    return 1 / (math.sqrt(f)) + 2 * math.log10(epsilon_DH / 3.7 + 2.51 / (Re[0] * math.sqrt(f)))

def equacao_colebrook_2(f):
    Re = 1*(10e5),
    epsilon_DH = 0.03
    return 1 / (math.sqrt(f)) + 2 * math.log10(epsilon_DH / 3.7 + 2.51 / (Re[0] * math.sqrt(f)))

def equacao_colebrook_3(f):
    Re = 3*(10e5),
    epsilon_DH = 0.01
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
print("\n"+ str(casos[0]))
print("Utilizando o método da secante conseguimos encontrar o valor: " + str(secantMethod(equacao_colebrook_1, 0.0001, 0.0003, 1e-6, 100)))
print("Utilizando o método da bissecção conseguimos encontrar o valor: " + str(bisectionMehod(equacao_colebrook_1, 0.0001, 1, 1e-6)))
print("\n"+ str(casos[1]))
print("Utilizando o método da secante conseguimos encontrar o valor: " + str(secantMethod(equacao_colebrook_2, 0.0001, 0.0003, 1e-6, 100)))
print("Utilizando o método da bissecção conseguimos encontrar o valor: " + str(bisectionMehod(equacao_colebrook_2, 0.0001, 1, 1e-6)))
print("\n"+ str(casos[2]))
print("Utilizando o método da secante conseguimos encontrar o valor: " + str(secantMethod(equacao_colebrook_3, 0.0001, 0.0003, 1e-6, 100)))
print("Utilizando o método da bissecção conseguimos encontrar o valor: " + str(bisectionMehod(equacao_colebrook_3, 0.0001, 1, 1e-6)))

print("\nAtividade 2_2 - 4")

def parabola_equation(x):
    return x**2 + 1

def elipse_equation(x):
    return 4 * np.sqrt(1 - (x**2))

x_values = np.linspace(-1.0, 1.0, 120, dtype='float64')

y_parabola = parabola_equation(x_values)
y_elipse = elipse_equation(x_values)

intersection_points_x = []
intersection_points_y = []

for x, y_p, y_e in zip(x_values, y_parabola, y_elipse):
    if np.isclose(round(y_p,1), round(y_e,1)):
        intersection_points_x.append(x)
        intersection_points_y.append(y_p)

# Plotar as curvas
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_parabola, label='Parábola: $y = x^2 + 1$')
plt.plot(x_values, y_elipse, label='Elipse: $\\frac{x^2}{1} + \\frac{y^2}{4} = 1$')
plt.scatter(intersection_points_x, intersection_points_y, color='red', label='Pontos de Interseção')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Interseção entre Parábola e Elipse')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 2.5)
plt.show()

# Exibir os pontos de interseção
print("Pontos de Interseção:")
for x, y in zip(intersection_points_x, intersection_points_y):
    print(f"({x:.4f}, {y:.4f})")
