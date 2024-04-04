from fastapi import APIRouter
from connection import firebase as db
from model.transaction_model import Transaction, Trans_ID

router = APIRouter()

# path = "/trans"

@router.post("/create")
async def create_trans(transaction: Transaction):
    path = f"trans/{transaction.phone_num}.json"
    res = db.update_data(path, transaction.model_dump())
    return res

@router.post("/read")
async def read_trans(transaction: Trans_ID):
    path = f"trans/{transaction.id}.json"
    res = db.get_data(path)
    return res

@router.post("/delete")
async def delete_trans(transaction: Trans_ID):
    path = f"trans/{transaction.id}.json"
    res = db.delete_data(path)
    return res