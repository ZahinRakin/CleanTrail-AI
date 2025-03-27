from fastapi import APIRouter, Request, Depends #type: ignore
from pydantic import BaseModel

from backend.models.user_model import User
from backend.controllers.user_controllers import (
  register,
  login,
  dummy_protected_route,
  refresh_access_token
)
from backend.middlewares.verifyJWT import verifyJWT

class LoginData(BaseModel):
  username: str
  password: str


router = APIRouter()

@router.post("/register")
async def register_user(user: User):
  return await register(user)
  
  
@router.get("/login")
async def login_user(login_data: LoginData):
  return await login(login_data)

@router.get("/dummy_protected_route")
async def dummy(req: Request, user: User = Depends(verifyJWT)):
  return await dummy_protected_route(user)

@router.get("/refresh-token")
async def refresh_token_(req: Request):
  access_token = req.headers["Authorization"][7:]
  return await refresh_access_token(access_token)
