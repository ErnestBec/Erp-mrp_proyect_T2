from utils.db import db_name
from fastapi import Response
from passlib.hash import sha256_crypt
from schemas.schema_user import userEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_user(user):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = db_name.Users.insert_one(new_user).inserted_id
    user = db_name.Users.find_one({"_id": id})
    return userEntity(user)


def get_user(id):
    user = db_name.Users.find_one({"_id": ObjectId(id)})
    return userEntity(user)


def update_user(id, user):
    db_name.Users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(db_name.Users.find_one({"_id": ObjectId(id)}))


def delete_user(id):
    db_name.Users.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
