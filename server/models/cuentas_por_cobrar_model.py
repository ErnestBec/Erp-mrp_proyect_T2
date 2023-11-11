from typing import Optional
from pydantic import BaseModel
from datetime import datetime
class Cuenta_por_cobrar(BaseModel):
    _id: Optional[str]
    solicitud: str
    importe: int
    fecha_emision: datetime
    total: int
    fecha_de_pago: datetime



class updateCuenta_por_cobrar(BaseModel):
    _id: Optional[str]
    solicitud: Optional[str]
    importe: Optional[int]
    fecha_emision: Optional[datetime]
    total: Optional[int]
    fecha_de_pago: Optional[datetime]

    

   