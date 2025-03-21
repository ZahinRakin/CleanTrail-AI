from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from .product_model import Product
from datetime import datetime, timezone
from pydantic import Field

class News(Document):
  product: Link[Product]
  title: str
  description: str
  created_at: datetime = Field(default_factory=lambda : datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
  
  async def save(self, *args, **kwargs):
    self.updated_at = datetime.now(timezone.utc)
    return await super().save(*args, **kwargs)
  
  class Settings:
    name = "news"