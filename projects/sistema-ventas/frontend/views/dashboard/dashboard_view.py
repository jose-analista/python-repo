# frontend/views/dashboard/dashboard_view.py
import flet as ft

def dashboard_view(page: ft.Page):
    """Vista del Dashboard principal"""
    
    page.controls.clear()
    
    # Verificar si está logueado
    user = page.session.get("user")
    if not user:
        page.go("/")
        return
    
    def logout(e):
        page.session.clear()
        page.go("/")
    
    page.add(
        ft.Row([
            ft.Text("📊 Dashboard", size=28, weight="bold"),
            ft.ElevatedButton("Cerrar Sesión", icon=ft.icons.LOGOUT, on_click=logout)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        ft.Divider(),
        
        ft.Text(f"Bienvenido, {user}!", size=20),
        ft.Container(height=20),
        
        # Tarjetas de resumen
        ft.Row([
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Ventas Hoy", size=14, color="grey"),
                        ft.Text("$0", size=28, weight="bold", color="green")
                    ]),
                    padding=20
                ),
                elevation=5
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Productos", size=14, color="grey"),
                        ft.Text("0", size=28, weight="bold", color="blue")
                    ]),
                    padding=20
                ),
                elevation=5
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Stock Bajo", size=14, color="grey"),
                        ft.Text("0", size=28, weight="bold", color="orange")
                    ]),
                    padding=20
                ),
                elevation=5
            ),
        ]),
        
        ft.Container(height=30),
        
        # Menú de navegación
        ft.Text("Accesos Rápidos", size=20, weight="bold"),
        ft.Row([
            ft.ElevatedButton(
                "🛒 Punto de Venta",
                icon=ft.icons.SHOPPING_CART,
                height=60,
                width=200,
                on_click=lambda e: page.go("/pos")
            ),
            ft.ElevatedButton(
                "📦 Inventario",
                icon=ft.icons.INVENTORY,
                height=60,
                width=200,
                on_click=lambda e: page.go("/inventory")
            ),
        ])
    )