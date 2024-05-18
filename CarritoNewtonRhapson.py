import numpy as np

# INGRESO
fx = lambda x: 0*x**7 - 0*x**6 + 0*x**5 - 0*x**4 + 0.01*x**3 - 0.08*x**2 + 1.15*x + 9.44



# Derivada de la función 
dfx = lambda x: 0.01*3*x**2 - 0.08*2*x + 1.15

x0 = 2
tolera = 0.001

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tramo)