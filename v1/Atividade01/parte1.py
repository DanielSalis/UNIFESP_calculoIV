import math
from math import e
import numpy as np
import matplotlib.pyplot as plt
from math import *
from newton_method import newton

# ***********************definindo funções e suas respectivas derivadas: ************************************


def f1(x):
    return x*(e**-x)


def diff_f1(x):
    return (1-x)*(e**-x)

# def f1(x):# f1_x0_1=5 #teste exemplo aula
#     return x**2-2
# def diff_f1(x):
#     return 2*x


def f2(x):
    return (x**(3))-x-3


def diff_f2(x):
    return (3*x)-1


def f3(x):
    return np.arctan(x)


def diff_f3(x):
    return 1/(1+(x**2))


# *******************************definindo parâmetros estabelecidos nos exercícios (x0, erro, maxit): **********************
f1_x0_1 = 2
f1_x0_2 = 0.5
f2_x0_1 = 1
f2_x0_2 = 2
f3_x0_1 = 1.45
f3_x0_2 = 1
erro = (10**(-8))
maxit = 20

# *******************************calculando utilizando método de Newton: **************************************************
res_f1_x0 = newton(f1, diff_f1, f1_x0_1, erro, maxit)
res_f1_x1 = newton(f1, diff_f1, f1_x0_2, erro, maxit)
res_f2_x0 = newton(f2, diff_f2, f2_x0_1, erro, maxit)
res_f2_x1 = newton(f2, diff_f2, f2_x0_2, erro, maxit)
res_f3_x0 = newton(f3, diff_f3, f3_x0_1, erro, maxit)
res_f3_x1 = newton(f3, diff_f3, f3_x0_2, erro, maxit)

print('Função 1, x0=2')
print(res_f1_x0)
print('\n Função 1, x0=0.5')
print(res_f1_x1)
print('\n Função 2, x0=1')
print(res_f2_x0)
print('\n Função 2, x0=2')
print(res_f2_x1)
print('\n Função 3, x0=1.45')
print(res_f3_x0)
print('\n Função 3, x0=1')
print(res_f3_x1)

# *******************************plotando os gráficos: **************************************************
# x1=np.linspace(-2,2)
# plt.figure()
# # plt.subplot(3, 1, 1)
# plt.title('Plot função 1')
# plt.plot(x1, f1(x1))
# plt.show()
# # plt.subplot(3, 1, 2)
# plt.figure()
# plt.title('Plot função 2')
# plt.plot(x1, f2(x1))
# # plt.scatter(x1, 0, color='red')
# plt.show()
# # plt.subplot(3, 1, 3)
# plt.figure()
# plt.title('Plot função 3')
# plt.plot(x1, f3(x1))
# plt.show()

# %% Parte2:


def f_parte2(x):
    e0 = 8.85*(10**(-12))
    F = 1.5
    p = 2*(10**-5)
    q = 5*(10**-5)
    constante = (4*math.pi*e0*F)/(p*q)
    return (x/(((x)**2)+1)**(1.5)) - constante


def diff_f_parte2(x):
    return (1/((((x)**2)+1)**(1.5))-((3*x)/((((x)**2)+1)**(2.5))))

# e0=8.85*(10**(-12))
# F=1.5
# p=2*(10**-5)
# q=5*(10**-5)
# numerador=(4*math.pi*e0*F)
# denominador=(p*q)
# constante=(4*math.pi*e0*F)/(p*q)
# print('numerador é: {}'.format(numerador))
# print('denominador é: {}'.format(denominador))
# print('constante é: {}'.format(constante))


x1 = np.linspace(-2, 2)
plt.figure()
plt.title('Plot função')
plt.plot(x1, f_parte2(x1))
plt.show()

# x0=0.3
# erro=(10**(-8))
# maxit=20

# questao4=newton(f_parte2,diff_f_parte2,x0,erro,maxit)
# print('Questão4, x0=0.3')
# print(questao4)

x0_questao6 = 0.7
erro_questao6 = (10**(-4))
maxit_questao6 = 10

questao6 = newton(f_parte2, diff_f_parte2, x0_questao6,
                  erro_questao6, maxit_questao6)
print('Questão6, x0=0.7')
print(questao6)

# %%
