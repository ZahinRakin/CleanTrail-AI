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
from .routes.g_auth_routes import router as g_auth_router


# have to delete later
# from .controllers.email_controllers import gmail_send_message


app = FastAPI()


origins=[
  "*"
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

app.include_router(healthcheck_router, prefix="/api/v1/healthcheck", tags=["healthcheck"])
app.include_router(user_router, prefix="/api/v1/user", tags=["user"])
app.include_router(store_owner_router, prefix="/api/v1/storeowner", tags=["storeowner"])
app.include_router(customer_router, prefix="/api/v1/customer", tags=["customer"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["admin"])
# app.include_router(store_router, prefix="/api/v1/store")this is still under consideration.
app.include_router(product_router, prefix="/api/v1/product", tags=["product"])
app.include_router(news_router, prefix="/api/v1/news", tags=["news"])
app.include_router(notification_router, prefix="/api/v1/notification", tags=["notification"])
app.include_router(g_auth_router, prefix="/auth/google", tags=["auth"])



# have to delete later when testing is done
# gmail_send_message()