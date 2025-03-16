from fastapi import APIRouter # type: ignore


router = APIRouter()

@router.get('/')
async def test():
  return {
    "message" : "OK"
  }