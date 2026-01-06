from sqlalchemy import Column, Integer, String, JSON
from ecommerce.app.db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=False)
    products = Column(JSON, nullable=False)
