# frontend/views/inventory/inventory_view.py
import flet as ft

def inventory_view(page: ft.Page):
    """Vista de Inventario"""
    
    page.controls.clear()
    
    user = page.session.get("user")
    if not user:
        page.go("/")
        return
    
    def go_back(e):
        page.go("/dashboard")
    
    page.add(
        ft.Row([
            ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
            ft.Text("📦 Inventario", size=28, weight="bold"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        ft.Divider(),
        
        ft.Text("Módulo de inventario en construcción...", size=16),
        ft.ElevatedButton("Volver al Dashboard", on_click=go_back)
    )