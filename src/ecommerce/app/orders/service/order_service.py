from ecommerce.app.orders.model.order import Order

class OrderService:
    def create_order(self, user, products):
        order = Order(user, products)
        return order.save()
