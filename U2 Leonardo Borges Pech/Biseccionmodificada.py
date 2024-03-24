from math import exp

def falsa_posicion(f, xl, xu, es, imax):
    iter = 0
    xr = xu
    ea = es + 1
    results = []

    while ea > es and iter < imax:
        xr_old = xr
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        iter += 1
        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            ea = 0
        
        results.append({
            'Iteracion': iter,
            'Xl': xl,
            'Xu': xu,
            'Xr': xr,
            'f(xl)': f(xl),
            'f(xu)': f(xu),
            'f(xr)': f(xr),
            'Ea': ea
        })

    return results

def velocidad_paracaidista(m):
    g = 9.8
    c = 15
    t = 9
    v = 35
    return (g * m / c) * (1 - exp(-c / m * t)) - v

xl = 59
xu = 60
es = 0.1
imax = 1000

results = falsa_posicion(lambda m: velocidad_paracaidista(m), xl, xu, es, imax)

# Iterar sobre los resultados y trabajar con ellos
for result in results:
    iteracion = result['Iteracion']
    xl = result['Xl']
    xu = result['Xu']
    xr = result['Xr']
    fxl = result['f(xl)']
    fxu = result['f(xu)']
    fxr = result['f(xr)']
    ea = result['Ea']
    # Aquí puedes hacer lo que necesites con los datos de cada iteración
    print(f"ITERACION {iteracion:02d}\tXL {xl:.9f}\tXU {xu:.9f}\tXR {xr:.9f}\t FXL {fxl:.9f}\t FXU {fxu:.9f}\t FXR {fxr:.9f}\t EA {ea:.9f}")
