
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
datos = pd.read_csv("datos/ventas.csv")

# Crear columna total
datos["total"] = datos["cantidad"] * datos["precio"]

# Calcular ventas totales
ventas_totales = datos["total"].sum()

# Producto más vendido
producto_mas_vendido = datos.groupby("producto")["cantidad"].sum().idxmax()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Ventas por producto
ventas_producto = datos.groupby("producto")["total"].sum()

# Crear gráfico
ventas_producto.plot(kind="bar")

# Título
plt.title("Ventas por producto")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado en resultados/")
