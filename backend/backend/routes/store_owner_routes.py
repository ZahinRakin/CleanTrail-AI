from fastapi import APIRouter

from backend.models.store_model import Store
from backend.models.product_model import Product
from backend.models.news_model import News
from backend.controllers.store_owner_controllers import(
  create_store,
  delete_store,
  
  create_product,
  delete_product,
  
  create_news,
  delete_news,
)



router = APIRouter()

@router.post("/store/create")
async def store_creation(store_data: Store):
  return await create_store(store_data)

@router.delete("/store/delete/{store_id}")
async def store_deletion(store_id: str):
  return await delete_store(store_id)

@router.post("/product/create")
async def product_creation(product_data: Product):
  return await create_product(product_data)

@router.delete("/product/delete")
async def product_deletion(product_id: str):
  return await delete_product(product_id)

@router.post("/news/create")
async def news_creation(news_data: News):
  return await create_news(news_data)

@router.delete("/news/delete")
async def news_deletion(news_id: str):
  return await delete_news(news_id)