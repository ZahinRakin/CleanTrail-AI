from fastapi import Request, HTTPException  # type: ignore
from jose import jwt  # type: ignore
import os
from backend.models.user_model import User

async def verifyJWT(request: Request):
    body = await request.json()  
    access_token = body.get("access_token") or request.headers.get("Authorization", "").removeprefix("Bearer ")

    if not access_token:
        raise HTTPException(status_code=401, detail="Access token is missing")

    try:
        decoded_token = jwt.decode(
            access_token,
            key=os.getenv("ACCESS_TOKEN_SECRET"),
            algorithms=[os.getenv("JWT_ALGORITHM")]
        )
        print(f"inside verifyJWT decoded token : {decoded_token}") # debugging log
        user_id = decoded_token.get('id')
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = await User.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    except jwt.JWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
