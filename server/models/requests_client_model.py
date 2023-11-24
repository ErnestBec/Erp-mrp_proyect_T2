from typing import Optional, List  # Permite omitir el ingreso de este datos
from pydantic import BaseModel


class products(BaseModel):
    id_pro: str
    quantity: int


class RequestsClient(BaseModel):
    _id: Optional[str]
    client: str
    products: List[products]
    date_delivery_expected: Optional[str]


class requestsClienteInsert(BaseModel):
    _id: Optional[str]
    status: Optional[str] = "pending"
    client: dict
    date_req: Optional[str]
    products: List[products]
    num_ref_solicitud: Optional[str]
    date_approved: Optional[str]
    date_delivery_expected: Optional[str]
    date_delivery: Optional[str]
