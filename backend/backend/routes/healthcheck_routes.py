from fastapi import APIRouter, Request, Depends # type: ignore
from backend.controllers.healthcheck_controllers import check_all
from backend.middlewares.verifyJWT import verifyJWT

router = APIRouter()


@router.post("/all")
async def do(request: Request):
  return await check_all()