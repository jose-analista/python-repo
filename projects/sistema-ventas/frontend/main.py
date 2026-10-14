# frontend/main.py
import flet as ft
from router import Router

def main(page: ft.Page):
    # Configuración global
    page.title = "Sistema de Ventas POS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 1200
    page.window.height = 800
    
    # Inicializar router
    router = Router(page)
    router.setup_routing()

if __name__ == "__main__":
    ft.app(target=main)