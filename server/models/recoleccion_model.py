from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Recoleccion(BaseModel):
    _id: Optional[str]
    fecha_recolection: datetime
    fecha_entrega: Optional[datetime]
    num_ref_solicictud: str
    cliente: str
    status: str
    costo: float


class updaterecoleccion(BaseModel):
    _id: Optional[str]
    fecha_recolection: Optional[datetime]
    fecha_entrega: Optional[datetime]
    num_ref_solicictud: str
    cliente: Optional[str]
    status: Optional[str]
    costo: Optional[float]
