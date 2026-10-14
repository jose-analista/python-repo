# frontend/router.py
import flet as ft
from views.auth.login_view import login_view
from views.pos.pos_view import pos_view
from views.inventory.inventory_view import inventory_view
from views.dashboard.dashboard_view import dashboard_view

class Router:
    """Maneja la navegación entre vistas"""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/": login_view,
            "/pos": pos_view,
            "/inventory": inventory_view,
            "/dashboard": dashboard_view
        }
    
    def navigate(self, route: str):
        """Navega a una ruta específica"""
        self.page.route = route
        self._handle_route()
    
    def _handle_route(self):
        """Maneja el cambio de ruta"""
        view_handler = self.routes.get(self.page.route, login_view)
        
        self.page.controls.clear()
        view_handler(self.page)
        self.page.update()
    
    def setup_routing(self):
        """Configura el enrutamiento"""
        self.page.on_route_change = lambda e: self._handle_route()
        self.page.go("/")