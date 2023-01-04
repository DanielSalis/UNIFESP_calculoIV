



#%% problema1.

def trapezios_repetida(funcao,inferior_a , superior_b , n):
    h=(superior_b-inferior_a)/n
    soma=0
    for k in range(1,n):
        soma+= (f(inferior_a+k*h))
    soma*=2
    soma+=(funcao(inferior_a)+funcao(superior_b))
    result=soma*(h/2)
    return result

import numpy as np
import math
from tabulate import tabulate

inferior_a , superior_b=0,math.pi/2
n=338

def f(x):
    return (2*math.cos(x/2))


# item a)
saida=[]
for i in range(2,13):
    n_resultado=(i)
    resultado=(trapezios_repetida(f,inferior_a,superior_b,i))
    saida.append([n_resultado,resultado])
    # print(f'n={i}: aproximação pelo método dos trapézios repetida= {resultado[i-2]}')

saida.append([n_resultado,resultado])
print(tabulate(saida,headers=["n","V aproximado"]))

#item b)
saida=[]
for i in range(2,13,2):
    n_resultado=(i)
    resultado=(trapezios_repetida(f,inferior_a,superior_b,i))
    saida.append([n_resultado,resultado])
    # print(f'n={i}: aproximação pelo método dos trapézios repetida= {resultado[i-2]}')

saida.append([n_resultado,resultado])
print(tabulate(saida,headers=["n","V aproximado"]))

#item c)
resultado=(trapezios_repetida(f,inferior_a,superior_b,n))
print(f'para n=338 V é aproximadamente: {resultado}')
erro_real=np.abs(resultado-2.82842712474619)
print(erro_real-(10**-6))

# if ((erro_real)<= 10**-6):
#     print(erro_real)
#     print(True)







#%% problema2.

def trapezios_repetida(funcao,inferior_a , superior_b , n):
    h=(superior_b-inferior_a)/n
    soma=0
    for k in range(1,n):
        soma+= (f(inferior_a+k*h))
    soma*=2
    soma+=(funcao(inferior_a)+funcao(superior_b))
    result=soma*(h/2)
    return result

import numpy as np
import math
from tabulate import tabulate

inferior_a , superior_b=1,5
n=12

def f(x):
    pi=math.pi
    p1=2*pi*math.sqrt(x)
    p2=1+((1/(2*math.sqrt(x)))**2)
    return (p1*math.sqrt(p2))

#item a)
saida=[]
for i in range(2,13):
    n_resultado=(i)
    resultado=(trapezios_repetida(f,inferior_a,superior_b,i))
    saida.append([n_resultado,resultado])
    # print(f'n={i}: aproximação pelo método dos trapézios repetida= {resultado[i-2]}')

# saida.append([n_resultado,resultado])
print(tabulate(saida,headers=["n","S aproximado"]))

#item b)
saida=[]
for i in range(2,13,2):
    n_resultado=(i)
    resultado=(trapezios_repetida(f,inferior_a,superior_b,i))
    saida.append([n_resultado,resultado])
    # print(f'n={i}: aproximação pelo método dos trapézios repetida= {resultado[i-2]}')

# saida.append([n_resultado,resultado])
print(tabulate(saida,headers=["n","S aproximado"]))



# %%
