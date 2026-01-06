
from fastapi import FastAPI
from ecommerce.app.orders.controller.order_controller import router as order_router
from ecommerce.app.db import database, Base, engine

app = FastAPI()

@app.on_event("startup")
async def startup():
	# Create tables if they do not exist
	Base.metadata.create_all(bind=engine)
	await database.connect()

@app.on_event("shutdown")
async def shutdown():
	await database.disconnect()

app.include_router(order_router)
