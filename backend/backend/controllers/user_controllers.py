from fastapi import Request, Response, HTTPException # type: ignore
from fastapi.encoders import jsonable_encoder # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from backend.utils.sanitize import sanitize_user_data
from backend.models.user_model import User
from jose import jwt # type: ignore
from backend.utils.token import gen_refresh_token
from backend.utils.token import gen_access_token
from passlib.context import CryptContext #type: ignore
import os
import json
from backend.models.user_model import User


pass_context = CryptContext(schemes="bcrypt", deprecated="auto")


async def register(user: User):  
  does_exist = bool(await User.find_one({
    "$or": [
      {"username": user.username},
      {"email": user.email}
    ]
  }))
  
  print(f"does the user exist = {does_exist}")
  if does_exist:
    raise HTTPException(status_code=400, detail="Username or email already in use") 
  
  new_user = User(**user.model_dump())
  
  new_user.refresh_token = await gen_refresh_token(str(new_user.id))
  await new_user.insert()
    
  return {"message": "successfully created user"}
  
  
  
async def login(req:Request):
  username, password = await req.json()
  username = username.strip()
  password = password.strip()
  
  user = await User.get_one(User.username == username)
  
  if not user:
    res.status_code = 404
    return {"message": "user not found"}
  
  if not pass_context.verify(password, user.password):
    res.status_code = 400
    return {"message": "password is wrong"}
  
  refresh_token = gen_refresh_token(user_id=user.id)
  print(f"inside login: refresh token: {refresh_token}") # debugging log
  access_token = gen_access_token(user)
  print(f"inside login: access token: {access_token}") # debugging log
  
  user.refresh_token = refresh_token
  await user.save()
  
  res.set_cookie(
    key = "refToken",
    value = refresh_token,
    httponly = True,
    secure = os.getenv("ENVIRONMENT") == "production",
    samesite = "Lax",
    max_age = os.getenv("COOKIE_MAX_AGE")
  )
  
  return {
    "access_token": access_token, 
    "message": "login successful"
  }
  
  