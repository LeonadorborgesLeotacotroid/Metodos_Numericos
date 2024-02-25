import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def calcular_velocidades():
    try:
        # Obtener datos del primer paracaidista del usuario
        m1 = float(entry_m1.get())
        c1 = float(entry_c1.get())

        # Obtener datos del segundo paracaidista del usuario
        m2 = float(entry_m2.get())
        c2 = float(entry_c2.get())

        # Gravedad
        g = 9.8  

        # Función de velocidad para el primer paracaidista
        def v1(t):
            return g * m1 / c1 * (1 - np.exp(-c1 / m1 * t))

        # Función de velocidad para el segundo paracaidista
        def v2(t):
            return g * m2 / c2 * (1 - np.exp(-c2 / m2 * t))

        # Tiempo
        t = np.linspace(0, 20, 100)

        # Velocidades
        v1_values = v1(t)
        v2_values = v2(t)

        # Gráfico de las velocidades
        plt.figure(figsize=(10, 6))
        plt.plot(t, v1_values, label='Velocidad del primer paracaidista')
        plt.plot(t, v2_values, label='Velocidad del segundo paracaidista')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Velocidad (m/s)')
        plt.title('Velocidad de los paracaidistas en caída libre con arrastre lineal')
        plt.legend()
        plt.grid(True)

        # Encontrar el tiempo en el que el segundo paracaidista alcanza la velocidad del primero a los 10 segundos
        t_igual_v1_10s = np.interp(v1(10), v2_values, t)
        plt.axvline(x=t_igual_v1_10s, color='gray', linestyle='--', label=f'{t_igual_v1_10s:.3f} segundos')
        plt.legend()

        plt.show()

        messagebox.showinfo("Resultado", f"El segundo paracaidista alcanza la velocidad del primero a los {t_igual_v1_10s:.3f} segundos.")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos para las masas y los coeficientes de arrastre.")

# Crear la ventana
root = tk.Tk()
root.title("Datos de los paracaidistas")

# Etiquetas y entradas para los datos de los paracaidistas
tk.Label(root, text="Masa del primer paracaidista (kg):").grid(row=0, column=0)
entry_m1 = tk.Entry(root)
entry_m1.grid(row=0, column=1)
tk.Label(root, text="Coeficiente de arrastre del primer paracaidista (kg/s):").grid(row=1, column=0)
entry_c1 = tk.Entry(root)
entry_c1.grid(row=1, column=1)

tk.Label(root, text="Masa del segundo paracaidista (kg):").grid(row=2, column=0)
entry_m2 = tk.Entry(root)
entry_m2.grid(row=2, column=1)
tk.Label(root, text="Coeficiente de arrastre del segundo paracaidista (kg/s):").grid(row=3, column=0)
entry_c2 = tk.Entry(root)
entry_c2.grid(row=3, column=1)

# Botón para calcular las velocidades
btn_calcular = tk.Button(root, text="Calcular velocidades", command=calcular_velocidades)
btn_calcular.grid(row=4, columnspan=2)


root.mainloop()
