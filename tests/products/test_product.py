from ecommerce.app.products import Product

def test_product_creation():
    p = Product("Book", 9.99)
    assert p.name == "Book"
    assert p.price == 9.99
