from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from starlette.requests import Request
from utils.db import db_name


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)},
                   key=getenv("SECRET"), algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    try:
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    return token


class Portador(HTTPBearer):
    async def __call__(self, request: Request):
        authorization = await super().__call__(request)
        validate_token(authorization.credentials)
        token = authorization.credentials
        token_data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        return token_data


class protectedAcountAdmin(HTTPBearer):
    async def __call__(self, request: Request):
        authorization = await super().__call__(request)
        token = authorization.credentials
        token_data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        user = db_name.Users.find_one(
            {"$and": [{"email": token_data["email"]}, {"status": "activate"}]})
        if not user:
            raise HTTPException(status_code=400, detail="user not account")
        if user["role"] == "client":
            raise HTTPException(status_code=400, detail="Access denied!")
        return user
