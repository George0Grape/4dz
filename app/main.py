from fastapi import FastAPI, HTTPException
from typing import List
app = FastAPI()
from .models import Product, ProductCreate, CartItem, Order
from .database import products, cart, orders
@app.get("/products/", response_model=List[Product])
def get_products():
    return products
@app.post("/products/", response_model=Product)
def add_product(product: ProductCreate):
    new_id = len(products) + 1
    new_product = Product(id=new_id, **product.dict())
    products.append(new_product)
    return new_product
@app.post("/cart/")
def add_to_cart(item: CartItem):
    product = next((p for p in products if p.id == item.product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < item.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")
    cart.append(item)
    return {"message": "Item added to cart"}
@app.get("/cart/", response_model=List[CartItem])
def get_cart():
    return cart
@app.post("/order/")
def place_order():
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")
    total_price = 0.0
    for item in cart:
        product = next((p for p in products if p.id == item.product_id), None)
        if product and product.stock >= item.quantity:
            product.stock -= item.quantity
            total_price += product.price * item.quantity
        else:
            raise HTTPException(status_code=400, detail=f"Not enough stock for product {product.name}")

    new_order = Order(id=len(orders) + 1, items=cart.copy(), total=total_price)
    orders.append(new_order)
    cart.clear()
    return {"message": "Order placed", "order_id": new_order.id, "total": total_price}
