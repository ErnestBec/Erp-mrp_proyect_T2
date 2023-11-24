from typing import Optional, List
from pydantic import BaseModel


class mp(BaseModel):
    id_mp: str
    name_mp: str
    quantyti: int


class Prducto(BaseModel):
    _id: Optional[str]
    name_prod: str
    Descripcion: str
    min_stock: int
    max_stock: int
    precio_uni: int
    num_pieza: str
    mp: List[mp]
    time_production: str


class updatePrducto(BaseModel):
    _id: Optional[str]
    name: Optional[str]
    Descripcion: Optional[str]
    min_stock: Optional[int]
    max_stock: Optional[int]
    precio_uni: Optional[int]
    num_pieza: Optional[str]
    mp: Optional[List[mp]]
    time_production: Optional[str]
