from fastapi import FastAPI # type:ignore
import uvicorn #type: ignore
from fastapi.middleware.cors import CORSMiddleware #type: ignore
from backend.routes.test_routes import router as test_router


app = FastAPI()
origins = [
  "http://localhost:5173",
  "http://localhost:5174",
  "http://localhost:5175",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(test_router, prefix="/api/v1/test")