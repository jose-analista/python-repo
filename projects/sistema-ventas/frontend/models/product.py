# frontend/models/product.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    category: str
    barcode: Optional[str] = None
    created_at: Optional[datetime] = None
    
    @property
    def is_low_stock(self) -> bool:
        """Regla de negocio: stock bajo"""
        return self.stock <= 5
    
    @property
    def is_available(self) -> bool:
        """Regla de negocio: disponible para venta"""
        return self.stock > 0
    
    def to_dict(self) -> dict:
        """Convierte a diccionario para enviar al backend"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
            "barcode": self.barcode
        }