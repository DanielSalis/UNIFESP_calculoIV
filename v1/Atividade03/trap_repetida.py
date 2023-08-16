import numpy as np
import math

def trapezios_repetida(funcao,inferior_a , superior_b , n):
    h=(superior_b-inferior_a)/n
    soma=0
    for k in range(1,n):
        soma+= (f(inferior_a+k*h))
    soma*=2
    soma+=(funcao(inferior_a)+funcao(superior_b))
    result=soma*(h/2)
    return result


