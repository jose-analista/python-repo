# prueba_flet.py
import flet as ft

def main(page: ft.Page):
    # Configuración básica de la ventana
    page.title = "Mi Primera App"
    page.theme_mode = ft.ThemeMode.DARK  # Modo oscuro automático
    page.window.width = 500
    page.window.height = 400
    page.padding = 30
    
    # Un texto grande
    titulo = ft.Text("¡Hola desde Flet!", size=30, weight="bold")
    
    # Un campo de texto (input)
    input_nombre = ft.TextField(label="¿Cómo te llamas?", width=300)
    
    # Un botón
    def saludar(e):
        saludo_text.value = f"¡Hola, {input_nombre.value}! 👋"
        saludo_text.visible = True
        page.update()
    
    btn = ft.ElevatedButton("Saludar", on_click=saludar)
    # Un texto que aparece al hacer clic
    saludo_text = ft.Text("", size=20, color="green", visible=False)
    
    # Agregamos todo a la ventana
    page.add(
        titulo,
        ft.Container(height=20),  # Espacio
        input_nombre,
        ft.Container(height=10),
        btn,
        ft.Container(height=20),
        saludo_text
    )

# Ejecutar la app
ft.app(target=main)