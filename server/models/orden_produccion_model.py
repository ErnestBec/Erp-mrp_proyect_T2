from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class product(BaseModel):
    id_prod: str
    quantity: int


class Orden_Produccion(BaseModel):
    _id: Optional[str]
    fecha_alta: datetime
    fecha_terminate: datetime
    products: List[product]
    status: Optional[str] = "pending"
    num_ref_solicitud: str


class updateorden_Prduccion(BaseModel):
    _id: Optional[str]
    fecha_alta: Optional[datetime]
    solicitud: Optional[int]
    producto: Optional[str]
    cantidad_fabri: Optional[int]
    id_pieza: Optional[int]
