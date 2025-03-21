from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from typing import List, Optional
from .store_model import Store


class StoreOwner(Document):
  stores: Optional[List[Link[Store]]] = None
  
  class Settings:
    name = "storeowners"