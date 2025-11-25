# proyecto_integracion_manual_final.py
# Métodos numéricos manuales: Trapecio, Simpson 1/3 y Simpson 3/8


import matplotlib.pyplot as plt

# --------------------------
# 1) Datos (31 puntos)
# --------------------------
x = [0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,
     2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,
     4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0]

C = [35.8026,33.7706,31.7389,29.707,27.6752,25.6435,23.6116,21.5799,19.5479,17.5162,
     15.4842,13.4525,10.963,9.3888,8.4511,7.5133,6.5756,5.6378,4.7001,3.7623,
     2.8246,1.8868,0.4571,0.0113,0.0101,0.0089,0.0076,0.0062,0.0049,0.0037,0.0025]

# --------------------------
# 2) Trapecio
# --------------------------
def trapecio(x, y):
    total = 0
    for i in range(len(x)-1):
        h = x[i+1] - x[i]
        total += h * (y[i] + y[i+1]) / 2
    return total

# --------------------------
# 3) Revisar malla uniforme
# --------------------------
def malla_uniforme(x, tol=1e-9):
    h0 = x[1] - x[0]
    for i in range(1, len(x)-1):
        if abs((x[i+1] - x[i]) - h0) > tol:
            return False, h0
    return True, h0

# --------------------------
# 4) Simpson 1/3
# --------------------------
def simpson_1_3(x, y):
    ok, h = malla_uniforme(x)
    if not ok:
        raise ValueError("Malla no uniforme")
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 requiere número de intervalos par")

    suma4 = sum(y[i] for i in range(1, n, 2))
    suma2 = sum(y[i] for i in range(2, n-1, 2))

    return (h/3) * (y[0] + y[-1] + 4*suma4 + 2*suma2)

# --------------------------
# 5) Simpson 3/8
# --------------------------
def simpson_3_8(x, y):
    ok, h = malla_uniforme(x)
    if not ok:
        raise ValueError("Malla no uniforme")
    n = len(x) - 1
    if n % 3 != 0:
        raise ValueError("Simpson 3/8 requiere múltiplo de 3")

    suma3 = 0
    suma2 = 0
    for i in range(1, n):
        if i % 3 == 0:
            suma2 += y[i]
        else:
            suma3 += y[i]

    return (3*h/8) * (y[0] + y[-1] + 3*suma3 + 2*suma2)

# --------------------------
# 6) Cálculos
# --------------------------
I_trap = trapecio(x, C)
I_s13  = simpson_1_3(x, C)
I_s38  = simpson_3_8(x, C)

print("\n=== RESULTADOS ===")
print("Trapecio     :", I_trap)
print("Simpson 1/3  :", I_s13)
print("Simpson 3/8  :", I_s38)

# --------------------------
# 7) Gráfica R2
# --------------------------
plt.figure(figsize=(10,5))
plt.plot(x, C, 'o-', label="Datos experimentales")
plt.xlabel("Distancia (m)")
plt.ylabel("Concentración (mg/m³)")
plt.title("Concentración vs Distancia")
plt.grid()
plt.legend()
plt.show()

# --------------------------
# 8) Área visual bajo la curva
# --------------------------
plt.figure(figsize=(10,4))
plt.plot(x, C, 'o-')
plt.fill_between(x, C, alpha=0.3)
plt.xlabel("Distancia (m)")
plt.ylabel("Concentración (mg/m³)")
plt.title("Área bajo la curva (∫C(x)dx)")
plt.grid()
plt.show()
