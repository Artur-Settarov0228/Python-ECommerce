from datetime import datetime
import json


class Product:
    
    def __init__(
            self,
            id: int,
            name: str,
            description: str,
            price: float,
            quantity: int,
            category: str,
            brand: str,
            in_stock: bool,
            created_at: datetime,
            updated_at: datetime,
        ):
        self.id          = id
        self.name        = name
        self.description = description
        self.price       = price
        self.quantity    = quantity
        self.category    = category
        self.brand       = brand
        self.in_stock    = in_stock
        self.created_at  = created_at
        self.updated_at  = updated_at

    def to_dict(self) -> dict:
       return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "brand": self.brand,
            "in_stock": self.in_stock,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity'],
            category=data['category'],
            brand=data['brand'],
            in_stock=data['in_stock'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ"),
            updated_at=datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%SZ"),
        )
    
    @classmethod
    def load_products(cls):
        with open("database/products.json") as jsonfile:
            data = json.load(jsonfile)

            products = []
            for item in data:
                products.append(cls.from_dict(item))

            return products
    