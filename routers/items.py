from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

class Item(BaseModel):
    id: int
    name: str

items = []

@router.get("/")
async def items_get():
    return items
