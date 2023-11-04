from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    _id: Optional[str]
    name: str
    email: str
    user: str
    password: str
    phone: int
    role: str = "client"
    status: str = "activate"


class updateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[int]
    role: Optional[str]
