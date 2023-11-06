from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Lote_Prod(BaseModel):
    fecha_prod: datetime
    mat_prod: int

class Rack(BaseModel):
    capacidad:int
    num_espacio:int

class Piso(BaseModel):
    num_piso:int
    num_fila:int
    rack:list[Rack]


class Lote_Almacen(BaseModel):
    tipo: str
    quantity_products: int
    piso:list[Piso]



 
class MateriaPrima(BaseModel):
    
    tipo: str
    quantity: int


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
    mp: list[MateriaPrima]
    lote_prod: list[Lote_Prod]
    lote_alamacen: list[Lote_Almacen]
    class Config:
        orm_mode = True


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
    lote_prod: Optional[list]
    lote_alamacen: Optional[list]
    

   