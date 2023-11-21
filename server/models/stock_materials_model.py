from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class typeStockModel(BaseModel):
    _id: Optional[str]
    name_type: str


class stock_products(BaseModel):
    _id: Optional[str]
    id_type_stock: str
    name_stock: str
    date_update: datetime


class rackModel(BaseModel):
    _id: Optional[str]
    id_stock: str
    name_rack: str
    width_capacity: int
    high_capacity: int
    long_capacity: int
    date_update: datetime


class Floors(BaseModel):
    _id: Optional[str]
    id_rack: str


class Rows(BaseModel):
    _id: Optional[str]
    id_floor: str


class SpaceRow(BaseModel):
    _id: str
    id_row: str
    id_prod: str
    status: Optional[str] = "free"


class product_pieza(BaseModel):
    _id: Optional[str]
    no_serie: str
    id_product: str
    status: str
    date: datetime
