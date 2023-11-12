from typing import Optional
from pydantic import BaseModel


class Prducto(BaseModel):
    _id: Optional[str]
    name_prod: str
    Descripcion: str
    min_stock: int
    max_stock: int
    precio_uni: int
    num_pieza: str
    category_prod: str
    cantidad_prod: int
    mp: list[dict[str, int]]


class updatePrducto(BaseModel):
    _id: Optional[str]
    name: Optional[str]
    Descripcion: Optional[str]
    min_stock: Optional[int]
    max_stock: Optional[int]
    precio_uni: Optional[int]
    num_pieza: Optional[str]
    category_prod: Optional[str]
    cantidad_prod: Optional[int]
    mp: Optional[list]
