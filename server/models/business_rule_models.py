from typing import Optional
from pydantic import BaseModel


class BusinnesRuleMaxProd(BaseModel):
    _id: Optional[str]
    max_prod: int
    min_prod: int
