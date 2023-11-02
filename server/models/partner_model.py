from typing import Optional  # Permite omitir el ingreso de este dato
from pydantic import BaseModel


class Patner(BaseModel):
    _id: Optional[str]
    name: str
    phone: int
    email: str
