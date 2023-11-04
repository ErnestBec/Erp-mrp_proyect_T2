from typing import Optional
from pydantic import BaseModel
class Prducto(BaseModel):
    _id: Optional[str]
    name: str
    Descripcion: str
    min_stock: int
    max_stock: int
    precio_uni: int
    num_pieza: int
    cantidad: int

class updatePrducto(BaseModel):
    _id: Optional[str]
    name: Optional[str]
    Descripcion: Optional[str]
    min_stock: Optional[int]
    max_stock: Optional[int]
    precio_uni: Optional[int]
    num_pieza: Optional[int]
    cantidad: Optional[int]
    