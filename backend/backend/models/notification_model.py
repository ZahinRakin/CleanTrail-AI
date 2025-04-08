from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from datetime import datetime, timezone
from pydantic import Field

from .user_model import User
from .product_model import Product


class Notification(Document):
  product: Link[Product]
  receiver: Link[User]
  title: str
  description: str
  created_at: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
  
  async def save(self, *args, **kwargs):
    self.updated_at = datetime.now(timezone.utc)
    return await super().save(*args, **kwargs)
  
  class Settings:
    name = "notifications"