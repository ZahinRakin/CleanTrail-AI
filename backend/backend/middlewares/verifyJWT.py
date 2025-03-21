from fastapi import Request #type: ignore

async def verifyJWT(request: Request):
  request.state.authorization = "authorized"
  return request