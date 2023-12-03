from pydantic import BaseModel
from typing import Optional


class PzaReq(BaseModel):
    id_pza: str
    quantity: int


class RequestSupply (BaseModel):
    _id: Optional[str]
    list_pzs: PzaReq[list]
    num_ref_request: str
