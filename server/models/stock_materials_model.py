from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


# class espacios(BaseModel):
#     numEspacio: str
#     cantidad: int


# class racks(BaseModel):
#     numRack: str
#     espacios: espacios
#     cantidad: int


# class filas(BaseModel):
#     numFila: str
#     racks: racks
#     cantidad: int


# class pisos(BaseModel):
#     num_piso: str
#     filas: filas
#     cantidad: int


# class stock_products(BaseModel):
#     _id: Optional[str]
#     quantity_total: int
#     pisos: pisos


# class stock_raw_materials(BaseModel):
#     _id: Optional[str]
#     quantity_total: int
#     pisos: pisos


# Modelo para Espacios en Rack
class RackSpace(BaseModel):
    name: str
    product_stored: str


# Modelo para Racks con espacios anidados
class Rack(BaseModel):
    name: str
    spaces: list[RackSpace]

# Modelo para Filas con racks anidados


class Row(BaseModel):
    name: str
    racks: list[Rack]

# Modelo para Pisos con filas anidadas


class Floor(BaseModel):
    name: str
    rows: list[Row]
