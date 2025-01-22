from pydantic import BaseModel

class CartItem(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
