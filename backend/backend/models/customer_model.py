from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from .user_model import User


class Customer(Document):
  user: Link[User]
  
  class Settings:
    name = "customers"