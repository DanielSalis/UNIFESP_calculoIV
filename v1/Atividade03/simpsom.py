import numpy as np
import math


def func(x):
    pi = math.pi
    p1 = 2*pi*math.sqrt(x)
    p2 = 1+((1/(2*math.sqrt(x)))**2)
    return (p1*math.sqrt(p2))


def simpson(func, a, b, subIntervalos):
    h = (b-a)/subIntervalos
    inicio = func(a)
    fim = func(b)

    x = a
    soma = 0
    for i in range(subIntervalos-1):
        x += h
        value = func(x)
        if i % 2 == 0:
            soma += 4 * value
        else:
            soma += 2 * value

    resultado = inicio+fim+soma
    total = (h/3)*(resultado)
    return total


print(simpson(func, 1, 5, 512))
