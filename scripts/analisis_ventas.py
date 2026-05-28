
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# Crear columna total
df["total"] = df["cantidad"] * df["precio"]

# Ventas totales
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Convertir fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Crear columna mes
df["mes"] = df["fecha"].dt.month

# Ventas por mes
ventas_por_mes = df.groupby("mes")["total"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

print("\nVentas por mes:")
print(ventas_por_mes)

# Crear gráfico
ventas_por_mes.plot(kind="bar")

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("\nGráfico guardado en resultados/")
