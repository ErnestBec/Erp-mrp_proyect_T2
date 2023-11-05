from pydantic import BaseModel


class stock_products():
    _id: str
    quantity_total: int
    pisos: list
    products: list


class stock_raw_materials():
    _id: str
    quantity_total: int
    pisos: list
    raws_materials: list
