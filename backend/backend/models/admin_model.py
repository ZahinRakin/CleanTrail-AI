from beanie import Document # type:ignore
from beanie.odm.fields import Link # type:ignore
from .user_model import User


class Admin(Document):
  user: Link[User]
  
  class Settings:
    name = "admins"