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
    no_floor: int


class Rows(BaseModel):
    _id: Optional[str]
    id_floor: str
    no_row: int


class SpaceRow(BaseModel):
    _id: str
    id_row: str
    no_space: str
    status: Optional[str] = "free"
