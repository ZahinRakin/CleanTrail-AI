from fastapi import APIRouter, Depends
from backend.middlewares.verifyJWT import verifyJWT
from backend.models.user_model import User


from backend.controllers.customer_controllers import (
  subscribe,
  unsubscribe
)


router = APIRouter()


@router.post("/subscribe/{product_id}")
async def subscribe_holder(product_id: str, user: User = Depends(verifyJWT)):
  return await subscribe(user.id, product_id)

@router.delete("/unsubscribe/{product_id}")
async def unsub_holder(product_id: str, user: User = Depends(verifyJWT)):
  return await unsubscribe(product_id, user)
