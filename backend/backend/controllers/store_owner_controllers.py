from backend.models.store_model import Store
from backend.models.product_model import Product
from backend.models.news_model import News


async def create_store(store_data):
  print(f"inside create store: {store_data}")  # debugging log
  store = await Store(**store_data.model_dump()).insert()
  return store
  
async def delete_store(store_id):
  print(f"inside delete store: {store_id}")  # debugging log
  response = await Store.get(store_id).delete()
  return response


async def create_product(product_data):
  print(f"inside create product: {product_data}")  # debugging log
  product = await Product(product_data.model_dump()).insert()
  return product
  
async def delete_product(product_id):
  print(f"inside delete product: {product_id}")  # debugging log  
  response = await Product.get(product_id).delete()
  return response


async def create_news(news_data):
  print(f"inside create news: {news_data}")  # debugging log
  news = await News(news_data.model_dump()).insert()
  return news
  
async def delete_news(news_id):
  print(f"inside delete news: {news_id}")  # debugging log
  response = await News.get(news_id).delete()
  return response