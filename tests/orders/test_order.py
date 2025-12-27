from ecommerce.app.orders import Order
from ecommerce.app.users import User
from ecommerce.app.products import Product

def test_order_creation():
    user = User("bob")
    products = [Product("Pen", 1.5)]
    order = Order(user, products)
    assert order.user.username == "bob"
    assert order.products[0].name == "Pen"
