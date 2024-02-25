import tkinter as tk
from tkinter import ttk
import math

def calcular_errores():
    try:
        x = float(entry_x.get())
        valor_exacto = math.exp(x)
        error_table.delete(*error_table.get_children())  # Limpiar la tabla antes de agregar nuevos valores
        inicio = int(spinbox_inicio.get())
        fin = int(spinbox_fin.get())
        for n in range(inicio, fin + 1):  # Calcular los errores para el rango seleccionado
            aproximacion = sum(x**i / math.factorial(i) for i in range(n))
            error_absoluto = abs(valor_exacto - aproximacion)
            error_relativo_porcentual = abs((valor_exacto - aproximacion) / valor_exacto) * 100
            error_table.insert("", "end", values=(n, aproximacion, error_absoluto, error_relativo_porcentual))
    except ValueError:
        label_resultado.config(text="Por favor ingresa un valor numérico para x")

# Crear la interfaz de tkinter
root = tk.Tk()
root.title("Calculadora de Errores para Serie de Taylor de e^x")

# Cuadro de entrada para el valor de x
label_x = tk.Label(root, text="Valor de x:")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

# Spinbox para seleccionar el rango de términos
label_terminos = tk.Label(root, text="Rango de Términos:")
label_terminos.pack()
spinbox_inicio = tk.Spinbox(root, from_=1, to=10, width=5)
spinbox_inicio.pack(side=tk.LEFT)
label_to = tk.Label(root, text="a")
label_to.pack(side=tk.LEFT)
spinbox_fin = tk.Spinbox(root, from_=1, to=10, width=5)
spinbox_fin.pack(side=tk.LEFT)

# Botón para calcular los errores
btn_calcular = tk.Button(root, text="Calcular Errores", command=calcular_errores)
btn_calcular.pack()

# Crear tabla para mostrar los resultados
error_table = ttk.Treeview(root, columns=("Término", "Aproximación", "Error Absoluto", "Error Relativo Porcentual"))
error_table.heading("#0", text="", anchor="w")
error_table.heading("Término", text="Término")
error_table.heading("Aproximación", text="Aproximación")
error_table.heading("Error Absoluto", text="Error Absoluto")
error_table.heading("Error Relativo Porcentual", text="Error Relativo Porcentual")
error_table.pack()

# Etiqueta para mensajes
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Ejecutar la aplicación
root.mainloop()
