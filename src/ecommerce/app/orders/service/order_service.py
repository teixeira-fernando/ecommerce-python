from ecommerce.app.orders.model.order import Order
from ecommerce.app.db import database
from sqlalchemy import insert

class OrderService:
    async def create_order(self, user, products):
        query = insert(Order).values(user=user, products=products).returning(Order.id, Order.user, Order.products)
        result = await database.fetch_one(query)
        if result:
            return dict(result)
        return None
