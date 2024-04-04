from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: str
    phone_num: str
    name: str
    address: str
    postcode: str
    order_id: str
    total_price: float
    status: str
    # order_date: datetime = datetime.now()
    
class Trans_ID(BaseModel):
    id: str