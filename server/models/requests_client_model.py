from typing import Optional  # Permite omitir el ingreso de este datos
from pydantic import BaseModel


class RequestsClient(BaseModel):
    _id: Optional[str]
    status: Optional[str] = "pending"
    num_ref: Optional[str]
    client: str
    products: list
    date_delivery_expected: Optional[str]


class requestsClienteInsert(BaseModel):
    _id: Optional[str]
    status: Optional[str] = "pending"
    client: dict
    date_req: Optional[str]
    product: dict
    num_ref: Optional[str]
    date_approved: Optional[str]
    date_delivery_expected: Optional[str]
    date_delivery: Optional[str]
