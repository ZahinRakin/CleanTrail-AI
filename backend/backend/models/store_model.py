from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from typing import List, Optional

from .product_model import Product


class Store(Document):
  name: str
  products: Optional[List[Link[Product]]] = []
  
  class Settings:
    name = "stores"