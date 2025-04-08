from fastapi import APIRouter

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
@router.delete("/store/delete")

@router.post("/product/create")
@router.delete("/product/delete")

@router.post("/news/create")
@router.delete("/news/delete")