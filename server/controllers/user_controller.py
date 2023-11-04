from utils.db import db_name
from fastapi import Response, HTTPException
from fastapi.responses import JSONResponse
from passlib.hash import sha256_crypt
from schemas.schema_user import userEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from middlewares.auth_middleware import write_token


def create_user(user):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = db_name.Users.insert_one(new_user).inserted_id
    user = db_name.Users.find_one({"_id": id})
    return JSONResponse(content={"user": userEntity(user), "status": "Successfull"}, status_code=201)


def get_user(id):
    user = db_name.Users.find_one({"_id": ObjectId(id)})
    return JSONResponse(content={"user": userEntity(user), "status": "Success!"}, status_code=201)


def update_user(id, user):
    db_name.Users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return JSONResponse(content={"status": "Update Successfull"}, status_code=204)


def delete_user(id, user):
    print(user)
    db_name.Users.find_one_and_delete(
        {"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)


def login(user):
    user_auth = db_name.Users.find_one(
        {"$and": [{"email": user["email"]}, {"status": "activate"}]})
    if not user_auth:
        raise HTTPException(status_code=400, detail="Credentials invalids!")

    # valid Password
    password = sha256_crypt.verify(user["password"], user_auth["password"])
    user_auth["password"]
    if not password:
        raise HTTPException(status_code=400, detail="Credentials invalids!")

    # Generate token
    token = write_token(user)
    return JSONResponse(content={"token": token, "status": "Succes Session!"}, status_code=201)
