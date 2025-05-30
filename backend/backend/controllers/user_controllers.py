from fastapi import Request, Response, HTTPException # type: ignore
from fastapi.encoders import jsonable_encoder # type: ignore
from fastapi.responses import JSONResponse # type: ignore

from backend.models import StoreOwner, Customer
from jose import jwt # type: ignore
from backend.utils.token import gen_refresh_token
from backend.utils.token import gen_access_token
from passlib.context import CryptContext #type: ignore
import os
from backend.models.user_model import User


pass_context = CryptContext(schemes="bcrypt", deprecated="auto")


async def register(user: User):

  print(f"inside register : user = {user}")  # debugging log
  try:
    if user.account_type == "storeowner":
      del user.account_type
      does_exist = bool(await StoreOwner.find_one({
        "$or": [
          {"username": user.username},
          {"email": user.email}
        ]
      }))
      if does_exist:
        raise HTTPException(status_code=400, detail="Username or email already in use")
      await StoreOwner(**user.model_dump()).insert()
    elif user.account_type == "client":
      del user.account_type
      does_exist = bool(await Customer.find_one({
        "$or": [
          {"username": user.username},
          {"email": user.email}
        ]
      }))
      if does_exist:
        raise HTTPException(status_code=400, detail="Username or email already in use")
      await Customer(**user.model_dump()).insert()
  except Exception as e:
    print(e)
    raise HTTPException(status_code=400, detail=str(e))
    
  return {"message": "successfully created user"}

async def login(login_data):
  user = await User.find_one(User.username == login_data.username)
  print(user)  # debugging log
  
  if not user:
    return JSONResponse(content={"message": "user not found"}, status_code=404)
  
  if not pass_context.verify(login_data.password, user.password):
    raise HTTPException( status_code=400, detail={"message": "password is wrong"})
  
  refresh_token = await gen_refresh_token(str(user.id))
  access_token = await gen_access_token(user)
  
  user.refresh_token = refresh_token
  await user.save()
  
  res = JSONResponse(
    content={
      "message": "login successful"
    },
    headers={"Authorization": f"Bearer {access_token}"}
  )
  res.set_cookie(
    key = "refreshToken",
    value = refresh_token,
    httponly = True,
    secure = os.getenv("ENVIRONMENT") == "production",
    samesite = "Lax",
    max_age = int(os.getenv("COOKIE_MAX_AGE"))
  )
  
  return res

async def dummy_protected_route(user):
  return {"user": user.username}
  
async def refresh_access_token(access_token: str):
  decoded_token = jwt.get_unverified_claims(access_token)
  
  user = await User.get(decoded_token.get("id"))
  if not user:
    raise HTTPException(status_code=404, detail="No user found. Is this a fabricated token?")

  new_access_token = await gen_access_token(user)

  return JSONResponse(
    content={
      "message": "Successfully refreshed the access token. token in header",
    },
    headers={"Authorization": f"Bearer {new_access_token}"}
  )

async def list_users():
    users = await User.find_all().to_list()
    return [user.dict() for user in users]

async def delete_user(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted successfully"}

async def get_user_details(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.dict()

