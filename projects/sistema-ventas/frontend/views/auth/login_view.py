# frontend/views/auth/login_view.py
import flet as ft

def login_view(page: ft.Page):
    """Vista de inicio de sesión responsiva y centrada"""
    
    page.controls.clear()
    
    # 1. COMPONENTES
    input_user = ft.TextField(
        label="Usuario",
        prefix_icon=ft.icons.PERSON,
    )
    
    input_pass = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
    )
    
    error_text = ft.Text("", color="red", visible=False, size=14)
    
    # 2. FUNCIÓN DE LOGIN
    def on_login_click(e):
        if input_user.value == "admin" and input_pass.value == "1234":
            page.session.set("user", input_user.value)
            page.go("/dashboard")
        else:
            error_text.value = "❌ Usuario o contraseña incorrectos"
            error_text.visible = True
            page.update()
    
    # 3. BOTÓN
    btn_login = ft.ElevatedButton(
        "Ingresar",
        icon=ft.icons.LOGIN,
        bgcolor="#2196F3",
        color="white",
        height=50,
        on_click=on_login_click
    )

    # 4. CONTENEDOR DEL FORMULARIO
    contenedor_login = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.SHOPPING_CART, color="#2196F3", size=36),
                ft.Text("Sistema de Ventas", size=28, weight="bold"),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Inicia sesión para continuar", size=14, color="grey", text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            input_user,
            input_pass,
            error_text,
            ft.Container(height=15),
            btn_login,
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH, 
        spacing=10,
        tight=True),
        padding=30,
        border=ft.border.all(1, "#444444"),
        border_radius=15,
        bgcolor="#1e1e1e",
        shadow=ft.BoxShadow(blur_radius=25, color="#00000060", spread_radius=2)
    )

    # 5. CONTENEDOR EXTERNO PARA CENTRADO VERTICAL
    # Este es el truco: un Column que ocupa toda la pantalla y centra su contenido
    contenedor_central = ft.Container(
        content=contenedor_login,
        alignment=ft.alignment.center,  # Centra el formulario dentro de este contenedor
        expand=True,                     # Ocupa todo el espacio disponible
    )

    # 6. FUNCIÓN RESPONSIVA
    def ajustar_ancho():
        max_ancho = 420
        ancho_disponible = page.window.width - 40
        
        if ancho_disponible < max_ancho:
            contenedor_login.width = page.window.width * 0.90
        else:
            contenedor_login.width = max_ancho
            
        # Ajustar título en pantallas muy pequeñas
        if page.window.width < 400:
            contenedor_login.content.controls[0].controls[1].size = 22
        else:
            contenedor_login.content.controls[0].controls[1].size = 28
            
        page.update()

    # 7. ENSAMBLAJE FINAL
    page.add(contenedor_central)
    
    # 8. ACTIVAR RESPONSIVIDAD
    ajustar_ancho()
    page.on_resize = lambda e: ajustar_ancho()