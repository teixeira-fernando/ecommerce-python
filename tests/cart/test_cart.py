from src.ecommerce.app.cart import Cart
from src.ecommerce.app.products import Product

def test_cart_add():
    cart = Cart()
    product = Product("Notebook", 2.5)
    cart.add(product)
    assert cart.items[0].name == "Notebook"
