from backend.models.store_model import Store
from backend.models.product_model import Product
from backend.models.news_model import News


async def create_store(store_data):
  store = await Store(store_data).insert()
  return store
  
async def delete_store(store_id):
  response = await Store.get(store_id).delete()
  return response


async def create_product(product_data):
  product = await Product(product_data).insert()
  return product
  
async def delete_product(product_id):
  response = await Product.get(product_id).delete()
  return response


async def create_news(news_data):
  news = await News(news_data).insert()
  return news
  
async def delete_news(news_id):
  response = await News.get(news_id).delete()
  return response