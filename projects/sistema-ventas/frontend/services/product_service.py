# frontend/services/product_service.py
import httpx
from typing import List, Optional
from models.product import Product

class ProductService:
    """Servicio para comunicarse con la API de productos"""
    
    def __init__(self, base_url: str = "http://localhost:8000/api/v1"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=10.0)
    
    async def get_all_products(self) -> List[Product]:
        """Obtiene todos los productos"""
        try:
            response = await self.client.get(f"{self.base_url}/products")
            response.raise_for_status()
            data = response.json()
            
            return [
                Product(
                    id=p["id"],
                    name=p["name"],
                    price=p["price"],
                    stock=p["stock"],
                    category=p["category"]
                )
                for p in data
            ]
        except httpx.HTTPError as e:
            print(f"Error al obtener productos: {e}")
            return []
    
    async def get_product_by_barcode(self, barcode: str) -> Optional[Product]:
        """Busca producto por código de barras"""
        try:
            response = await self.client.get(
                f"{self.base_url}/products/barcode/{barcode}"
            )
            response.raise_for_status()
            data = response.json()
            
            return Product(
                id=data["id"],
                name=data["name"],
                price=data["price"],
                stock=data["stock"],
                category=data["category"],
                barcode=data.get("barcode")
            )
        except httpx.HTTPError:
            return None