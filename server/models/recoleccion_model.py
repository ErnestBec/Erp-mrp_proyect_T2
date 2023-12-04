from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class Recoleccion(BaseModel):
    _id: Optional[str]
    fecha_recolection: datetime
    fecha_entrega: Optional[datetime]
    num_ref_solicitud: str
    cliente: str
    status: str
    costo: float


class updaterecoleccion(BaseModel):
    _id: Optional[str]
    fecha_recolection: Optional[datetime]
    fecha_entrega: Optional[datetime]
    num_ref_solicitud: str
    cliente: Optional[str]
    status: Optional[str]
    costo: Optional[float]


class ObjectMp(BaseModel):
    id_mp: str
    quantity: int


class ReceivedEmbark(BaseModel):
    _id: Optional[str]
    num_ref_solicitud: str
    list_Mp: List[ObjectMp]
