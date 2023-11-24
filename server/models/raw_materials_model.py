from typing import Optional
from pydantic import BaseModel


class raw_materials(BaseModel):
    _id: Optional[str]
    tipo: str
    quantity: int
    min_stock: int = 11
    max_stock: int = 100
    id_space_Rack: int


class updateraw_materials(BaseModel):
    _id: Optional[str]
    tipo: Optional[str]
    quantity: Optional[int]
    min_stock: Optional[int]
    max_stock: Optional[int]
    id_space_Rack: Optional[int]
