from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from datetime import datetime, timezone
from pydantic import Field
from typing import Optional, List
from .customer_model import Customer


class Product(Document):
  name: str
  description: Optional[str] = None
  image: Optional[str] = None
  subscribers: Optional[List[Link[Customer]]] = None
  created_at: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
  
  async def save(self, *args, **kwargs):
    self.updated_at = datetime.now(timezone.utc)
    return await super().save(*args, **kwargs)
  
  class Settings:
    name = "products"