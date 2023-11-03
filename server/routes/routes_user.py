from fastapi import APIRouter, Response
from utils.db import db_name
from schemas.schema_user import userEntity, usersEntity
from models.user_model import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()


@user.get("/users")
def find_all_user():
    return usersEntity(db_name.Users.find())


@user.post("/user")
def create_user(user: User):
    new_user = dict(user)
    # del new_user["_id"]
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = db_name.Users.insert_one(new_user).inserted_id
    user = db_name.Users.find_one({"_id": id})
    return userEntity(user)


@user.get("/users/{id}")
def find_user(id: str):
    return userEntity(db_name.Users.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}")
def update_user(id: str, user: User):
    db_name.Users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(db_name.Users.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}")
def delete_user(id: str):
    userEntity(db_name.Users.find_one_and_delete(
        {"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
