from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from typing import List

from .product_model import Product


class Store(Document):
  name: str
  products: List[Link[Product]]
  
  class Settings:
    name = "stores"