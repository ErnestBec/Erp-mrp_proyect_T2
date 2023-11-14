from pydantic import BaseModel
from datetime import date
from typing import Optional


class typeStockModel(BaseModel):
    _id: Optional[str]
    name_type: str


class stock_products():
    _id: Optional[str]
    type_stock: str
    name_stock: int
    date_update: date


class rackModel(BaseModel):
    _id: Optional[str]
    id_stock: str
    name_rack: str
    width_capacity: int
    high_capacity: int
    long_capacity: int
    update_date: date


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
    status: Optional[str]
