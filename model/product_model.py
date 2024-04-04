from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    pic_url: str
    price: float
    stock: int
    category: str
    
class Product_ID(BaseModel):
    id: str