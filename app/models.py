from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    items: List[CartItem]
    total: float
