from fastapi import HTTPException

from backend.models.store_model import Store
from backend.models.product_model import Product
from backend.models.news_model import News


async def create_store(store_data):
  print(f"inside create store: {store_data}")  # debugging log
  store = await Store(**store_data.model_dump()).insert()
  return store
  

async def delete_store(store_id):
  store = await Store.get(store_id)
  if not store:
    raise HTTPException(status_code=404, detail="Store not found")
  await store.delete()
  return {"message": "Store deleted successfully"}


async def create_product(product_data):
  print(f"inside create product: {product_data}")  # debugging log
  product = await Product(**product_data.model_dump()).insert()
  return product
  
async def delete_product(product_id):
  print(f"inside delete product: {product_id}")  # debugging log  
  product = await Product.get(product_id)
  if product:
    await product.delete()
    return {"message": "successfully deleted the product."}
  raise HTTPException(status_code=404, detail="product not found")


async def create_news(news_data):
  print(f"inside create news: {news_data}")  # debugging log
  news = await News(**news_data.model_dump()).insert()
  return news
  
async def delete_news(news_id):
  print(f"inside delete news: {news_id}")  # debugging log
  news = await News.get(news_id)
  if news:
    await news.delete()
    return {"message": "successfully deleted the news"}
  raise HTTPException(status_code=404, detail="news not found")