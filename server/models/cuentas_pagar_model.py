from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Cuenta_Pagar(BaseModel):
    _id: Optional[str]
    proveedor: dict
    importe: int
    fecha_de_pago: datetime
    status: str


class updateCuentaPagar(BaseModel):
    _id: Optional[str]
    proveedor: Optional[str]
    solicitud: [int]
    importe: Optional[int]
    total: Optional[int]
    fecha_de_pago: Optional[datetime]
