from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


products = [
    Product(id=1, name="Молоко", price=50.0, stock=10),
    Product(id=2, name="Хлеб", price=30.0, stock=15),
    Product(id=3, name="Яблоки", price=70.0, stock=20),
    Product(id=4, name="Бананы", price=60.0, stock=25),
    Product(id=5, name="Масло сливочное", price=120.0, stock=8),
    Product(id=6, name="Сыр", price=200.0, stock=12),
    Product(id=7, name="Кефир", price=55.0, stock=18),
    Product(id=8, name="Куриные яйца", price=80.0, stock=30),
    Product(id=9, name="Рис", price=90.0, stock=14),
    Product(id=10, name="Макароны", price=45.0, stock=22),
    Product(id=11, name="Картофель", price=40.0, stock=50),
    Product(id=12, name="Морковь", price=35.0, stock=40),
    Product(id=13, name="Лук репчатый", price=25.0, stock=35),
    Product(id=14, name="Помидоры", price=80.0, stock=18),
    Product(id=15, name="Огурцы", price=70.0, stock=20),
    Product(id=16, name="Конфеты", price=150.0, stock=10),
    Product(id=17, name="Шоколад", price=100.0, stock=15),
    Product(id=18, name="Чай черный", price=250.0, stock=7),
    Product(id=19, name="Кофе растворимый", price=300.0, stock=9),
    Product(id=20, name="Вода минеральная 1л", price=40.0, stock=40)
]
cart = []
orders = []