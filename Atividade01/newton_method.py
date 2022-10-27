import numpy as np
from tabulate import tabulate

#o método de Newton função newton tem como entrada a função f, a derivada da função f denominada diff_funcao, o ponto inicial x0, a tolerância e o número máximo de iterações.
def newton(funcao,diff_funcao,x0,erro,maxit):
    k=0
    xk=x0
    xanterior=0
    fk=funcao(x0)
    fk=np.abs(fk)
    derivadafk=diff_funcao(x0)
    derivadafk=np.abs(derivadafk)
    sk=1
    saida=[]
    saida.append([k,xk,fk,sk])
    while(np.abs(fk)>erro and k<maxit and np.abs(sk)>erro):
        xanterior=xk
        xk=xk-(fk/derivadafk)
        sk=xk-xanterior
        k=k+1
        fk=funcao(xk)
        derivadafk=diff_funcao(xk)
        saida.append([k,xk,fk,np.abs(sk)])
        #apenas para verificar por qual motivo é a aproximação mais assertiva:
        if np.abs(fk)<erro:
            print('esse np.abs(fk)<erro')
        if np.abs(sk)<erro:
            print('esse np.abs(sk)>erro')
    # return saida
    return tabulate(saida, headers=["k", "xk", "f(xk)",'stepk'])