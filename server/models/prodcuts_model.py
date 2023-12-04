from typing import Optional, List
from pydantic import BaseModel


class mp(BaseModel):
    id_mp: str
    name_mp: str
    quantyti: float


class Prducto(BaseModel):
    _id: Optional[str]
    name_prod: str
    Descripcion: str
    min_stock: int
    max_stock: int
    precio_uni: int
    mp: List[mp]
    time_production: float


class updatePrducto(BaseModel):
    _id: Optional[str]
    name: Optional[str]
    Descripcion: Optional[str]
    min_stock: Optional[int]
    max_stock: Optional[int]
    precio_uni: Optional[int]
    mp: Optional[List[mp]]
    time_production: Optional[float]
