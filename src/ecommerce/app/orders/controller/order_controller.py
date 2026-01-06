from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ecommerce.app.orders.service.order_service import OrderService

router = APIRouter()

class OrderRequest(BaseModel):
    user: str
    products: list[str]

class OrderResponse(BaseModel):
    id: int
    user: str
    products: list[str]

@router.post("/orders", response_model=OrderResponse)
async def create_order(order_req: OrderRequest):
    service = OrderService()
    order = await service.create_order(order_req.user, order_req.products)
    if not order:
        raise HTTPException(status_code=400, detail="Order creation failed")
    return OrderResponse(id=order["id"], user=order["user"], products=order["products"])
