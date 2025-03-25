from fastapi import APIRouter, Request #type: ignore

from backend.models.user_model import User
from backend.controllers.user_controllers import (
  register,
  login
)


router = APIRouter()

@router.post("/register")
async def register_user(user: User):
  return await register(user)
  
  
@router.get("/login")
async def login_user(req: Request):
  return await login(req)