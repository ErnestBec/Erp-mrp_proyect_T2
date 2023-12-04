from typing import Optional
from pydantic import BaseModel


class raw_materials(BaseModel):
    _id: Optional[str]
    Name: str
    min_stock: int = 11
    max_stock: int = 100


class updateraw_materials(BaseModel):
    _id: Optional[str]
    Name: Optional[str]
    min_stock: Optional[int]
    max_stock: Optional[int]
