
# 📘 **README – Proyecto de Integración Numérica y Procesamiento de Datos**

**Curso:** Procesos Numéricos
**Autor:** David Pelaez
**Año:** 2025

---

## 🧩 **Descripción del Proyecto**

Este proyecto implementa métodos de **integración numérica hechos completamente a mano** , con base en datos experimentales de **concentración de ácido acético** en función de la **distancia**.

El objetivo principal es calcular el **área bajo la curva concentración vs distancia**, lo cual representa la **masa lineal aproximada del contaminante**.

Se aplican los siguientes métodos:

* Método del **Trapecio compuesto**
* Método de **Simpson 1/3 compuesto**
* Método de **Simpson 3/8 compuesto**

Además, se generan **gráficas** basadas en los datos experimentales.

---

## 📂 **Estructura del Proyecto**

```
/proyecto_procNum_c3
│
├── proyecto.py       # Script principal
├── Datos.txt                             # Archivo CSV con resultados numéricos
└── README.md                             # Este documento
```

---

## 🧠 **Marco Teórico en el que nos basamos**

Este proyecto está fundamentado en:

### ✔ **Ley de Fick de la Difusión**

Modela la disminución de concentración en función de la distancia y el tiempo.

* **Primera Ley:** flujo proporcional al gradiente de concentración
* **Segunda Ley:** describe cómo la concentración evoluciona en el tiempo

### ✔ **Conversión de unidades**

Se usa:
[
mg/m^3 = ppm \times 2.5
]

### ✔ **Interpretación física de la integral**

El área bajo la curva:

[
M = \int_{x_0}^{x_f} C(x), dx
]

representa la **masa lineal total** del ácido acético en el tramo analizado.

---

## 🧪 **Datos Utilizados**

Se usan **31 puntos experimentales** correspondientes a:

* Distancia desde la fuente (0 a 6 m)
* Concentración en mg/m³


---

## 🛠️ **Métodos Numéricos Implementados (Manual)**

Todos los métodos fueron implementados manualmente (solo se usa `matplotlib` para graficar):

### 🔹 **1. Trapecio compuesto**

Acepta malla no uniforme.

### 🔹 **2. Simpson 1/3 compuesto**

Requiere:

* Malla uniforme
* Número par de segmentos

### 🔹 **3. Simpson 3/8 compuesto**

Requiere:

* Malla uniforme
* Número de segmentos múltiplo de 3

---

## ▶ **Instrucciones de Ejecución**

### Requisitos

* Python 3.10+
* Matplotlib (solo para graficación)

Instalar si es necesario:

```bash
pip install matplotlib
```

### Ejecutar

```bash
python proyecto_integracion_manual.py
```

El script:

* Imprime los valores de las integrales en consola
* Genera 2 gráficas:

  * Concentración vs distancia
  * Área bajo la curva
* Crea el archivo:

```
resultados_integracion_manual.csv
```

---

## 📊 **Resultados Generados**

El codigo ncluye los valores obtenidos con:

* Trapecio compuesto
* Simpson 1/3
* Simpson 3/8

Las gráficas permiten visualizar:

1. Cómo disminuye la concentración al aumentar la distancia
2. La interpretación física del área bajo la curva

---

## 🖼️ **Visualización**

El programa genera dos gráficas separadas:

* Una de los datos originales de concentración
* Otra del área bajo la curva sombreada

Para ver la segunda gráfica, debes cerrar la primera ventana (esto es comportamiento normal de matplotlib).

---

## 🚀 **Conclusiones**

* Los métodos de integración manual implementados permiten estimar la masa lineal del contaminante con precisión.
* Simpson 1/3 y Simpson 3/8 muestran mayor exactitud respecto al método del Trapecio.
* Las gráficas permiten interpretar correctamente el comportamiento típico de difusión (disminución exponencial).

---

## 📞 **Hecho por: **

**Autor:** David Pelaez

