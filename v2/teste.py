import numpy as np
import matplotlib.pyplot as plt

# Definir a equação da parábola e da elipse
def parabola(x):
    return x**2 + 1

def elipse(x):
    return 4 * np.sqrt(1 - (x**2))

# Criar um intervalo de valores de x para calcular os pontos de interseção
x_values = np.linspace(-1.0, 1.0, 120, dtype='float64')

# Calcular os valores correspondentes de y para a parábola e a elipse
y_parabola = parabola(x_values)
y_elipse = elipse(x_values)

# Encontrar os pontos de interseção
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


# F([x y]) = [y - (x^2 + 1) ]
#            [x^2 + (y^2 / 4) - 1]

