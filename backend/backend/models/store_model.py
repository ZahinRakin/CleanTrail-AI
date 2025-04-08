from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from typing import List, Optional
from pydantic import Field

from .product_model import Product


class Store(Document):
  name: str
  products: Optional[List[Link[Product]]] = Field(default_factory=list)
  
  class Settings:
    name = "stores"