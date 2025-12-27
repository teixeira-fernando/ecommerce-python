from ecommerce.app.cart import Cart
from ecommerce.app.products import Product

def test_cart_add():
    cart = Cart()
    product = Product("Notebook", 2.5)
    cart.add(product)
    assert cart.items[0].name == "Notebook"
