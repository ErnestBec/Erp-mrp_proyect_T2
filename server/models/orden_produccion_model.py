from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Orden_Produccion(BaseModel):
    _id: Optional[str]
    fecha_alta: datetime
    solicitud: int
    producto: str
    cantidad_fabri: int
    id_pieza: int



class updateorden_Prduccion(BaseModel):
    _id: Optional[str]
    fecha_alta: Optional[datetime]
    solicitud: Optional[int]
    producto: Optional[str]
    cantidad_fabri: Optional[int]
    id_pieza: Optional[int]

    

   