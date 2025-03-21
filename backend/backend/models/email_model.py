from beanie import Document # type:ignore
from datetime import datetime, timezone
from pydantic import Field


class Email(Document):
  sender: str
  receiver: str
  subject: str
  body: str
  created_at: datetime = Field(default_factory= lambda : datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory= lambda : datetime.now(timezone.utc))
  
  async def save(self, *args, **kwargs):
    self.updated_at = datetime.now(timezone.utc)
    return await super().save(*args, **kwargs)
  
  class Settings:
    name = "emails"