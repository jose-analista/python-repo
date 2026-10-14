# caja_registradora.py
import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURACIÓN DE LA VENTANA
    page.title = "Caja Registradora Simple"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 600
    page.window.height = 650
    page.padding = 20

    # 2. ESTADO DE LA APLICACIÓN (Variables que guardan datos)
    carrito = []
    total = 0.0

    # 3. COMPONENTES DE LA INTERFAZ (UI)
    
    # Inputs para ingresar datos (como si fueras el cajero)
    input_producto = ft.TextField(
        label="Nombre del producto", 
        width=300,
        hint_text="Ej: Leche 1L"
    )
    input_precio = ft.TextField(
        label="Precio ($)", 
        width=150, 
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Ej: 1200"
    )
    
    # Tabla para mostrar el carrito de compras
    tabla_carrito = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Producto", weight="bold")),
            ft.DataColumn(ft.Text("Precio", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")),
        ],
        rows=[] # Se llenará dinámicamente
    )

    # Texto grande para el total
    texto_total = ft.Text("Total: $0", size=28, weight="bold", color="green")

    # 4. LÓGICA Y FUNCIONES
    
    def agregar_producto(e):
        nonlocal total  # Permite modificar la variable 'total' de afuera
        
        nombre = input_producto.value.strip()
        precio_str = input_precio.value.strip()
        
        # Validación simple
        if not nombre or not precio_str:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Debes ingresar nombre y precio"), open=True)
            page.update()
            return
            
        try:
            precio = float(precio_str)
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ El precio debe ser un número"), open=True)
            page.update()
            return

        # Agregar a la lista y sumar al total
        carrito.append({"nombre": nombre, "precio": precio})
        total += precio
        
        # Agregar fila a la tabla visual
        # Usamos una función lambda para pasar el índice y poder borrarlo después
        tabla_carrito.rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(nombre)),
                ft.DataCell(ft.Text(f"${precio:,.0f}")), # Formato sin decimales
                ft.DataCell(ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color="red", 
                                          on_click=lambda e, idx=len(carrito)-1: eliminar_producto(idx)))
            ])
        )
        
        # Limpiar los inputs y devolver el foco al primero (como un lector de código de barras)
        input_producto.value = ""
        input_precio.value = ""
        input_producto.focus() 
        
        # Actualizar el total en pantalla
        texto_total.value = f"Total: ${total:,.0f}"
        page.update()

    def eliminar_producto(index):
        nonlocal total
        # Restar el precio del total y quitar de la lista
        total -= carrito[index]["precio"]
        carrito.pop(index)
        
        # Quitar la fila de la tabla
        tabla_carrito.rows.pop(index)
        
        texto_total.value = f"Total: ${total:,.0f}"
        page.update()

    def cobrar(e):
        if total == 0:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ El carrito está vacío"), open=True)
            page.update()
            return
            
        # Mostrar mensaje de éxito en la parte inferior
        page.snack_bar = ft.SnackBar(
            ft.Text(f"✅ ¡Venta realizada con éxito por ${total:,.0f}!"), 
            bgcolor="green", 
            open=True
        )
        
        # Reiniciar todo para la siguiente venta
        carrito.clear()
        tabla_carrito.rows.clear()
        total = 0.0
        texto_total.value = "Total: $0"
        page.update()

    # 5. ENSAMBLAJE (Dibujar todo en la pantalla)
    page.add(
        ft.Text("🛒 Punto de Venta (POS)", size=28, weight="bold"),
        ft.Divider(),
        
        # Fila de inputs y botón de agregar
        ft.Row([
            input_producto, 
            input_precio, 
            ft.ElevatedButton("Agregar", icon=ft.icons.ADD, on_click=agregar_producto)
        ]),
        
        ft.Divider(),
        
        # La tabla del carrito
        tabla_carrito,
        
        ft.Divider(),
        
        # Fila del total y botón de cobrar
        ft.Row([
            texto_total, 
            ft.ElevatedButton("💵 COBRAR", bgcolor="green", color="white", height=50, on_click=cobrar)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )
    
    # Poner el cursor en el primer input al iniciar
    input_producto.focus()

# Ejecutar la app
ft.app(target=main)