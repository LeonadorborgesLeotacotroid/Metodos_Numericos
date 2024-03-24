import numpy as np
import matplotlib.pyplot as plt

# INGRESO de la funcion juntona la der
fx = lambda x: x**2 - 2*x - 3
dfx = lambda x: 2*x - 2

x0 = 2
tolera = 0.001

# PROCEDIMIENTO
tabla = []
tramo = abs(2 * tolera)
xi = x0
while tramo >= tolera:
    xnuevo = xi - fx(xi) / dfx(xi)
    tramo = abs(xnuevo - xi)
    error_verdadero = abs((xnuevo - xi) / xnuevo) * 100 if xnuevo != 0 else 0
    tabla.append([xi, xnuevo, tramo, error_verdadero])
    xi = xnuevo

# convierte la lista a un arreglo
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print('Iteración   xi          xnuevo      tramo             error verdadero')
np.set_printoptions(precision=15, suppress=True)
for i in range(n):
    print(f'{i + 1:<11}{tabla[i, 0]:<12.6f}{tabla[i, 1]:<12.6f}{tabla[i, 2]:<18.6f}{tabla[i, 3]:<18.6f}')
print('\nraiz en:', xi)
print('con error de:', tramo)

# Gráfica de la función y la raíz
x = np.linspace(-10, 10, 400)
y = fx(x)
plt.plot(x, y, label='f(x) = x^2 - 2x - 3')
plt.scatter(tabla[:, 0], np.zeros(n), color='blue', label='Iteraciones')
plt.scatter(xi, 0, color='red', label='Raíz encontrada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Método de Newton-Raphson')
plt.show()
