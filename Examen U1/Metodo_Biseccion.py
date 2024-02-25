import tkinter as tk
from tkinter import ttk

def Bisect(xl, xu, es, imax):
    xr = 0
    iter = 0
    ea = 100
    data = []
    while True:
        xrold = xr
        xr = (xl + xu) / 2
        iter += 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        et = abs((0.5671 - xr) / 0.5671) * 100  # Calcula Et basado en el valor real
        data.append([iter, xl, xu, xr, ea, et])
        if ea < es or iter >= imax:
            break
    return data

def f(x):
    return -4*x**2 + 5*x + 1

def mostrar_tabla():
    xl = 0
    xu = 2
    es = 0.5
    imax = 100
    result_data = Bisect(xl, xu, es, imax)

    root = tk.Tk()
    root.title("Tabla de Iteraciones")

    tree = ttk.Treeview(root, columns=("Iter", "xl", "xu", "xr", "ea", "et"))
    tree.heading("#0", text="Index")
    tree.heading("Iter", text="Iter")
    tree.heading("xl", text="xl")
    tree.heading("xu", text="xu")
    tree.heading("xr", text="xr")
    tree.heading("ea", text="ea")
    tree.heading("et", text="et")
    
    for i, row in enumerate(result_data):
        tree.insert("", "end", text=str(i), values=(row[0], row[1], row[2], row[3], row[4], row[5]))

    tree.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()

mostrar_tabla()
