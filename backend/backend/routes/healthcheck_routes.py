from fastapi import APIRouter, Request, Depends # type: ignore
from backend.controllers.healthcheck_controllers import check_all
from backend.middlewares.verifyJWT import verifyJWT

router = APIRouter()


@router.post("/all", dependencies=[Depends(verifyJWT)])
async def do(request: Request):
  print("is authorized: ", request.state.authorization)
  return await check_all()