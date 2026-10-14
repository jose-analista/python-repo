# frontend/views/pos/pos_view.py
import flet as ft
from viewmodels.pos_viewmodel import POSViewModel

def pos_view(page: ft.Page):
    """Vista del Punto de Venta"""
    
    # Inicializar ViewModel
    vm = POSViewModel()
    
    # === COMPONENTES DE LA UI ===
    
    # Buscador de productos
    search_field = ft.TextField(
        label="Buscar producto o escanear código",
        prefix_icon=ft.icons.SEARCH,
        autofocus=True,
        width=400,
        on_change=lambda e: _on_search_change(e.control.value)
    )
    
    # Lista de resultados de búsqueda
    search_results = ft.ListView(spacing=5, expand=False)
    
    # Tabla del carrito
    cart_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Producto", weight="bold")),
            ft.DataColumn(ft.Text("Precio", weight="bold")),
            ft.DataColumn(ft.Text("Cant.", weight="bold")),
            ft.DataColumn(ft.Text("Subtotal", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")),
        ],
        rows=[]
    )
    
    # Texto del total
    total_text = ft.Text("Total: $0", size=28, weight="bold", color="green")
    
    # Mensaje de error
    error_text = ft.Text("", color="red", visible=False)
    
    # === FUNCIONES DE EVENTOS (conectan View con ViewModel) ===
    
    async def _on_search_change(query: str):
        """Cuando el usuario escribe en el buscador"""
        results = await vm.search_product(query)
        
        search_results.controls.clear()
        
        for product in results[:10]:  # Mostrar máx 10 resultados
            stock_color = "red" if product.is_low_stock else "green"
            stock_text = f"({product.stock} disp.)"
            
            row = ft.ListTile(
                leading=ft.Icon(ft.icons.SHOPPING_BAG),
                title=ft.Text(product.name),
                subtitle=ft.Text(
                    f"${product.price:,.0f} {stock_text}",
                    color=stock_color
                ),
                on_click=lambda e, p=product: _add_product_to_cart(p)
            )
            search_results.controls.append(row)
        
        page.update()
    
    def _add_product_to_cart(product):
        """Agregar producto al carrito"""
        success = vm.add_to_cart(product)
        
        if success:
            _refresh_cart_table()
            search_field.value = ""
            search_results.controls.clear()
            page.update()
        else:
            error_text.value = vm.error_message
            error_text.visible = True
            page.update()
    
    def _refresh_cart_table():
        """Actualiza la tabla del carrito"""
        cart_table.rows.clear()
        
        for i, item in enumerate(vm.get_cart_items()):
            product = item["product"]
            quantity = item["quantity"]
            subtotal = item["subtotal"]
            
            cart_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(product.name)),
                    ft.DataCell(ft.Text(f"${product.price:,.0f}")),
                    ft.DataCell(ft.Text(str(quantity))),
                    ft.DataCell(ft.Text(f"${subtotal:,.0f}")),
                    ft.DataCell(
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            icon_color="red",
                            on_click=lambda e, idx=i: _remove_from_cart(idx)
                        )
                    )
                ])
            )
        
        total_text.value = f"Total: ${vm.get_total():,.0f}"
    
    def _remove_from_cart(index: int):
        """Eliminar producto del carrito"""
        vm.remove_from_cart(index)
        _refresh_cart_table()
        page.update()
    
    def _checkout(e):
        """Procesar pago"""
        if vm.get_total() == 0:
            error_text.value = "⚠️ El carrito está vacío"
            error_text.visible = True
            page.update()
            return
        
        # Aquí iría la lógica para enviar la venta al backend
        page.snack_bar = ft.SnackBar(
            ft.Text(f"✅ Venta completada por ${vm.get_total():,.0f}"),
            bgcolor="green",
            open=True
        )
        vm.clear_cart()
        _refresh_cart_table()
        page.update()
    
    # === ENSAMBLAJE DE LA VISTA ===
    
    page.add(
        ft.Row([
            ft.Text("🛒 Punto de Venta", size=28, weight="bold"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        ft.Divider(),
        
        # Buscador y resultados
        ft.Row([search_field]),
        ft.Container(
            content=search_results,
            height=200,
            border=ft.border.all(1, "grey"),
            border_radius=5,
            visible=False  # Se muestra cuando hay búsqueda
        ),
        
        ft.Divider(),
        
        # Carrito
        ft.Text("Carrito de Compras", size=20, weight="bold"),
        cart_table,
        
        ft.Divider(),
        
        # Total y botón de cobrar
        ft.Row([
            total_text,
            ft.ElevatedButton(
                "💵 COBRAR",
                bgcolor="green",
                color="white",
                height=50,
                width=200,
                on_click=_checkout
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        error_text
    )
    
    # Cargar productos al iniciar
    page.run_task(vm.load_products)