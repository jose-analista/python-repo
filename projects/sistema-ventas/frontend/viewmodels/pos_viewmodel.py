# frontend/viewmodels/pos_viewmodel.py
from typing import List, Dict
from models.product import Product
from services.product_service import ProductService

class POSViewModel:
    """ViewModel para el Punto de Venta"""
    
    def __init__(self):
        self.product_service = ProductService()
        self.cart: List[Dict] = []
        self.total: float = 0.0
        self.products: List[Product] = []
        self.search_query: str = ""
        self.error_message: str = ""
    
    async def load_products(self):
        """Carga productos desde la API"""
        self.products = await self.product_service.get_all_products()
    
    async def search_product(self, query: str) -> List[Product]:
        """Busca productos por nombre o código de barras"""
        self.search_query = query
        
        if not query:
            return self.products
        
        # Filtrar localmente (luego puede ser búsqueda en API)
        results = [
            p for p in self.products 
            if query.lower() in p.name.lower() 
            or (p.barcode and query in p.barcode)
        ]
        
        return results
    
    def add_to_cart(self, product: Product, quantity: int = 1):
        """Agrega producto al carrito"""
        if not product.is_available:
            self.error_message = f"❌ Producto '{product.name}' agotado"
            return False
        
        if product.stock < quantity:
            self.error_message = f"️ Stock insuficiente. Solo hay {product.stock} unidades"
            return False
        
        # Verificar si ya está en el carrito
        for item in self.cart:
            if item["product"].id == product.id:
                item["quantity"] += quantity
                self._calculate_total()
                self.error_message = ""
                return True
        
        # Agregar nuevo item
        self.cart.append({
            "product": product,
            "quantity": quantity,
            "subtotal": product.price * quantity
        })
        
        self._calculate_total()
        self.error_message = ""
        return True
    
    def remove_from_cart(self, index: int):
        """Elimina producto del carrito"""
        if 0 <= index < len(self.cart):
            self.cart.pop(index)
            self._calculate_total()
    
    def _calculate_total(self):
        """Calcula el total del carrito"""
        self.total = sum(item["subtotal"] for item in self.cart)
    
    def clear_cart(self):
        """Limpia el carrito"""
        self.cart.clear()
        self.total = 0.0
    
    def get_cart_items(self) -> List[Dict]:
        """Retorna items del carrito para la UI"""
        return self.cart
    
    def get_total(self) -> float:
        """Retorna el total formateado"""
        return self.total