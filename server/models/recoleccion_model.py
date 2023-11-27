from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Recoleccion(BaseModel):
    _id: Optional[str]
    fecha: datetime
    lugar: str
    id_pago: str
    status: str


class updaterecoleccion(BaseModel):
    _id: Optional[str]
    fecha: Optional[datetime]
    lugar: Optional[str]
    id_cobro: Optional[int]
    status: Optional[str]
