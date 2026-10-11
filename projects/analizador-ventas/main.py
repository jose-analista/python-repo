
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
df = pd.read_csv("projects/analizador-ventas/ventas.csv")

# Calcular el total de cada venta
df["total"] = df["cantidad"] * df["precio"]

# Mostrar los datos
print("\n=== DATOS DE VENTAS ===")
print(df)

# Calcular las ventas por producto
ventas_producto = df.groupby("producto")["total"].sum()

print("\n=== VENTAS POR PRODUCTO ===")
print(ventas_producto)

# Mostrar las ventas totales
print("\nVentas totales:", ventas_producto.sum())

# Identificar el producto con mayores ingresos
producto_top = ventas_producto.idxmax()
print("Producto con mayores ingresos:", producto_top)

# Crear un gráfico
ventas_producto.plot(kind="bar", color="steelblue")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas en pesos")
plt.xticks(rotation=0)
plt.tight_layout()

# Mostrar el gráfico
plt.show()