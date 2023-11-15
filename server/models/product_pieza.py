from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class product_pieza(BaseModel):
    _id: Optional[str]
    id_product: str
    status: str
    date: datetime
