from typing import Optional
from pydantic import BaseModel


class raw_materials(BaseModel):
    _id: Optional[str]
    raw_material: str
    quatity: int
    min_stock: int = 11
    max_stock: int = 100
