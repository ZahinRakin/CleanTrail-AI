from fastapi import APIRouter, Request #type: ignore

from backend.controllers.user_controllers import (
  register,
  login
)


router = APIRouter()

@router.post("/register")
async def register_user(req: Request):
  return await register(req)
  
  
@router.get("/login")
async def login_user(req: Request):
  return await login(req)