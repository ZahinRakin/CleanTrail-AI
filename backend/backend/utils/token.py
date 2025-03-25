from jose import jwt # type: ignore
from datetime import datetime, timezone, timedelta
import os


async def gen_refresh_token(user_id: str):
  payload = {
    "id": user_id,
    "exp": datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("REFRESH_DURATION_MINUTES")))
  }
  return jwt.encode( # this is a synchronous program so no await
    claims=payload, 
    key=os.getenv("REFRESH_TOKEN_SECRET"), 
    algorithm=os.getenv("JWT_ALGORITHM")
  )

async def gen_access_token(user):
  payload = {
    "id": str(user.id),
    "username": user.username,
    "email": user.email,
    "exp": datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_DURATION_MINUTES")))
  }
  
  return jwt.encode(claims=payload, key=os.getenv("ACCESS_TOKEN_SECRET"), algorithm=os.getenv("JWT_ALGORITHM"))