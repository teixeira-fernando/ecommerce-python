from ecommerce.app.payments import Payment
from ecommerce.app.orders import Order
from ecommerce.app.users import User
from ecommerce.app.products import Product

def test_payment_creation():
    user = User("eve")
    products = [Product("Bag", 20.0)]
    order = Order(user, products)
    payment = Payment(order, 20.0)
    assert payment.amount == 20.0
    assert payment.order.user.username == "eve"
