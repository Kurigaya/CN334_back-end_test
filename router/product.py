from fastapi import APIRouter
from connection import firebase as db
from model.product_model import Product, Product_ID

router = APIRouter()

# path = 'product/'

@router.post('/create')
async def create_product(product: Product):
    path = f"product/{product.id}.json"
    res = db.update_data(path, product.model_dump())
    return res

@router.post("/read")
async def read_product(product: Product_ID):
    path = f"product/{product.id}.json"
    res = db.get_data(path)
    return res

@router.post("/delete")
async def delete_product(product: Product_ID):
    path = f"product/{product.id}.json"
    res = db.delete_data(path)
    return res