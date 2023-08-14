from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str
    price: float

@router.post('/estimate')
async def estimate(item: Item):
    return {'status': 'success', 'datax': item }