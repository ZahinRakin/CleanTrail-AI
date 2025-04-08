from backend.models.user_model import User
from backend.models.product_model import Product
from backend.models.notification_model import Notification
from fastapi import HTTPException


async def subscribe(product_id: str, user: User):
  try:
    product = await Product.get(product_id)
    product.subscribers.append(user)
  except Exception as e:
    raise HTTPException(status_code=503, detail=str(e))

async def unsubscribe(product_id: str, user: User):
  try:
    product = await Product.get(product_id)
    product.subscribers.remove(user)
  except Exception as e:
    print(f"inside unsubscribe. Error: {e}")
    raise HTTPException(status_code=503, detail=str(e))
  
async def notifiy_me(product_id: str, user_id: str, title: str, description: str):
  try:
    await Notification(
      product=product_id,
      receiver=user_id,
      title=title,
      description=description
    ).insert()
  except Exception as e:
    print(f"inside notifyme. Error: {e}")  
  