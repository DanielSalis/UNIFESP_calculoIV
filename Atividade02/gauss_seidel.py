import math
from tabulate import tabulate


def get_normres(x, xk):
    current_sum = 0
    arrays_tuple = zip(x, xk)
    for x_i, xk_i in arrays_tuple:
        current_sum += math.fabs(x_i-xk_i)

    return current_sum


def get_normrel(x, xk):
    # sempre pegando a primeira posicao
    x_i = x[0]
    xk_i = xk[0]
    normrel = math.fabs(xk_i - x_i) / math.fabs(xk_i)

    return normrel


def compare(current_eps, eps):
    if (current_eps < eps):
        return True
    else:
        return False


def run(A, b, x_array, max_iterations, eps):
    saida = []
    b_array_length = len(b)
    has_soluction = True
    x = x_array.copy()
    for i in list(range(0, b_array_length, 1)):
        if (math.fabs(A[i][i]) > 0.0):
            x[i] = b[i]/A[i][i]
        else:
            has_soluction = False
            break

    if (has_soluction):
        xk = x.copy()
        current_iteraction = 0

        while (current_iteraction < max_iterations):
            current_iteraction += 1
            for i in list(range(0, b_array_length, 1)):
                current_sum = 0
                for j in list(range(0, b_array_length, 1)):
                    if (i != j):
                        current_sum += A[i][j]*xk[j]
                    elif (i < j):
                        current_sum += A[i][j]*x[j]

                xk[i] = (1/A[i][i])*(b[i]-current_sum)

            current_eps = get_normres(x, xk)
            current_normrel = get_normrel(x, xk)
            saida.append([current_iteraction, current_eps, current_normrel])
            if compare(current_eps, eps):
                x = xk.copy()
                break
            if compare(current_normrel, eps):
                x = xk.copy()
                break
            x = xk.copy()

    print(tabulate(saida, headers=["k", "normres", "normrel"]))
    return x
