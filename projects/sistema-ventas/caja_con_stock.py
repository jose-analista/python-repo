# caja_con_stock.py
import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURACIÓN DE LA VENTANA
    page.title = "Caja Registradora con Control de Stock"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 700
    page.window.height = 700
    page.padding = 20

    # 2. BASE DE DATOS SIMULADA (INVENTARIO)
    # En un sistema real, esto vendría de una base de datos (SQLite/PostgreSQL)
    inventario = {
        "leche": {"nombre": "Leche 1L", "precio": 1200, "stock": 3},      # ¡Stock bajo!
        "pan": {"nombre": "Pan Hallulla", "precio": 1500, "stock": 5},    # ¡Stock bajo!
        "cerveza": {"nombre": "Cerveza Cristal", "precio": 2000, "stock": 24},
        "galletas": {"nombre": "Galletas Chocolate", "precio": 1800, "stock": 50},
        "azucar": {"nombre": "Azúcar 1kg", "precio": 1300, "stock": 0}    # ¡Agotado!
    }

    # 3. ESTADO DE LA APLICACIÓN
    carrito = []
    total = 0.0

    # 4. COMPONENTES DE LA INTERFAZ (UI)
    input_producto = ft.TextField(
        label="Nombre del producto", 
        width=300,
        hint_text="Ej: leche, pan, cerveza",
        autofocus=True,
        on_change=lambda e: auto_completar_precio(e.control.value) # ¡Magia!
    )
    
    input_precio = ft.TextField(
        label="Precio ($)", 
        width=150, 
        keyboard_type=ft.KeyboardType.NUMBER,
        read_only=True # El precio lo sacamos del inventario, el cajero no lo escribe
    )
    
    tabla_carrito = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Producto", weight="bold")),
            ft.DataColumn(ft.Text("Precio", weight="bold")),
            ft.DataColumn(ft.Text("Stock Restante", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")),
        ],
        rows=[]
    )

    texto_total = ft.Text("Total: $0", size=28, weight="bold", color="green")

    # 5. LÓGICA Y FUNCIONES
    
    def auto_completar_precio(nombre):
        """Busca el producto en el inventario y rellena el precio automáticamente."""
        nombre_key = nombre.lower().strip()
        if nombre_key in inventario:
            input_precio.value = str(inventario[nombre_key]["precio"])
            page.update()

    def agregar_producto(e):
        nonlocal total
        
        nombre_input = input_producto.value.strip().lower()
        precio_str = input_precio.value.strip()
        
        if not nombre_input or not precio_str:
            mostrar_alerta("⚠️ Ingresa un producto válido", "orange")
            return
            
        try:
            precio = float(precio_str)
        except ValueError:
            mostrar_alerta("⚠️ El precio debe ser un número", "orange")
            return

        # --- LÓGICA DE INVENTARIO ---
        if nombre_input in inventario:
            producto_db = inventario[nombre_input]
            nombre_real = producto_db["nombre"]
            stock_actual = producto_db["stock"]
            
            if stock_actual <= 0:
                mostrar_alerta(f"🚫 ¡AGOTADO! No hay más '{nombre_real}' en inventario.", "red")
                return
            
            if stock_actual <= 5:
                mostrar_alerta(f"⚠️ ¡STOCK BAJO! Solo quedan {stock_actual} unidades de '{nombre_real}'.", "orange")
            
            # Descontar del inventario
            inventario[nombre_input]["stock"] -= 1
            stock_restante = inventario[nombre_input]["stock"]
        else:
            # Si es un producto nuevo, lo agregamos al inventario con stock 10 por defecto
            nombre_real = input_producto.value.strip().title()
            inventario[nombre_input] = {"nombre": nombre_real, "precio": precio, "stock": 9}
            stock_restante = 9
            mostrar_alerta(f"ℹ️ Producto nuevo '{nombre_real}' agregado al inventario.", "blue")

        # Agregar al carrito
        carrito.append({"nombre": nombre_real, "precio": precio})
        total += precio
        
        # Determinar color del stock en la tabla
        color_stock = "red" if stock_restante <= 5 else "green"
        texto_stock = f"{stock_restante} uds." if stock_restante > 0 else "AGOTADO"

        # Agregar fila a la tabla
        indice_actual = len(carrito) - 1
        tabla_carrito.rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(nombre_real)),
                ft.DataCell(ft.Text(f"${precio:,.0f}")),
                ft.DataCell(ft.Text(texto_stock, color=color_stock, weight="bold")),
                ft.DataCell(ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color="red", 
                                          on_click=lambda e, idx=indice_actual: eliminar_producto(idx)))
            ])
        )
        
        # Limpiar y preparar para el siguiente
        input_producto.value = ""
        input_precio.value = ""
        input_producto.focus()
        texto_total.value = f"Total: ${total:,.0f}"
        page.update()

    def eliminar_producto(index):
        nonlocal total
        item = carrito[index]
        total -= item["precio"]
        carrito.pop(index)
        tabla_carrito.rows.pop(index)
        
        # (Opcional) Devolver el stock al inventario si se cancela la venta
        # inventario[nombre]["stock"] += 1 
        
        texto_total.value = f"Total: ${total:,.0f}"
        page.update()

    def cobrar(e):
        if total == 0:
            mostrar_alerta("⚠️ El carrito está vacío", "orange")
            return
            
        mostrar_alerta(f"✅ ¡Venta realizada con éxito por ${total:,.0f}!", "green")
        
        # Reiniciar
        carrito.clear()
        tabla_carrito.rows.clear()
        total = 0.0
        texto_total.value = "Total: $0"
        page.update()

    def mostrar_alerta(mensaje, color):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensaje), 
            bgcolor=color, 
            open=True
        )
        page.update()

    # 6. ENSAMBLAJE DE LA INTERFAZ
    page.add(
        ft.Row([
            ft.Text("🛒 Punto de Venta con Stock", size=28, weight="bold"),
            ft.Icon(ft.icons.INVENTORY_2, color="blue", size=32)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(),
        
        ft.Row([
            input_producto, 
            input_precio, 
            ft.ElevatedButton("Agregar", icon=ft.icons.ADD, on_click=agregar_producto)
        ]),
        
        ft.Container(height=10),
        ft.Text("💡 Tip: Escribe 'leche', 'pan' o 'azucar' para probar las alertas de stock.", size=12, color="grey"),
        
        ft.Divider(),
        tabla_carrito,
        ft.Divider(),
        
        ft.Row([
            texto_total, 
            ft.ElevatedButton("💵 COBRAR", bgcolor="green", color="white", height=50, width=200, on_click=cobrar)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

ft.app(target=main)