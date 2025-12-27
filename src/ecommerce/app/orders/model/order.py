class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products
        self.id = None

    def save(self):
        self.id = 1
        return self
