from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import os

from .DB.connectDB import connectDB

from .routes.user_routes import router as user_router
from .routes.store_owner_routes import router as store_owner_router
from .routes.customer_routes import router as customer_router
from .routes.admin_routes import router as admin_router
from .routes.product_routes import router as product_router
from .routes.news_routes import router as news_router
from .routes.notification_routes import router as notification_router
from .routes.healthcheck_routes import router as healthcheck_router


app = FastAPI()


origins=[
  "http://localhost:5173",
  "http://localhost:5174",
  "http://localhost:5175"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.on_event("startup") # from contextlib import asynccontextmanager
async def startup_event():
  await connectDB()

@app.on_event("shutdown")
async def shutdown_event():
  for key in list(os.environ.keys()):
    os.environ.pop(key, None)

app.include_router(healthcheck_router, prefix="/api/v1/healthcheck")
app.include_router(user_router, prefix="/api/v1/user")
app.include_router(store_owner_router, prefix="/api/v1/storeowner")
app.include_router(customer_router, prefix="/api/v1/customer")
app.include_router(admin_router, prefix="/api/v1/admin")
# app.include_router(store_router, prefix="/api/v1/store")this is still under consideration.
app.include_router(product_router, prefix="/api/v1/product")
app.include_router(news_router, prefix="/api/v1/news")
app.include_router(notification_router, prefix="/api/v1/notification")