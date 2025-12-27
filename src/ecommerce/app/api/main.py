from fastapi import FastAPI

from ecommerce.app.orders.controller.order_controller import router as order_router

app = FastAPI()

app.include_router(order_router)
