from utils.db import db_name
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from passlib.hash import sha256_crypt
from schemas.schema_user import userEntity, userEntityUpdate
from bson import ObjectId
from middlewares.auth_middleware import write_token


def create_user(user):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = db_name.Users.insert_one(new_user).inserted_id
    user = db_name.Users.find_one({"_id": id})
    return JSONResponse(content={"user": userEntity(user), "status": "Successfull"}, status_code=201)


def get_user(id):
    user = db_name.Users.find_one({"_id": ObjectId(id)})
    print(user["_id"])
    return JSONResponse(content={"user": userEntity(user), "status": "Success!"}, status_code=201)


def update_user(id, user, userSession):
    print(user["email"])
    print(userSession["email"])

    update = db_name.Users.find_one_and_update(
        {"$and": [{"_id": ObjectId(id)}, {"email": userSession["email"]}]}, {"$set": dict(user)})
    print(update)
    if update == None:
        raise HTTPException(
            status_code=400, detail="You can only edit your account!")
    else:
        return JSONResponse(content={"status": "Update Successfull", "user": user}, status_code=201)


def delete_user(id, user):
    print(user)
    db_name.Users.find_one_and_delete(
        {"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)


def login(user):
    user_auth = db_name.Users.find_one(
        {"$and": [{"email": user["email"]}, {"status": "activate"}]})

    if not user_auth:
        return JSONResponse(status_code=400, content={
            "status": "Credentials invalids!"})

    # valid Password
    password = sha256_crypt.verify(user["password"], user_auth["password"])
    
    if not password:
        return JSONResponse(status_code=400, content={
            "status": "Credentials invalids!"})

    # Generate token
    token = write_token(user)
    return JSONResponse(content={"token": token,"role":user_auth["role"], "status": "Succes Session!"}, status_code=201)


def get_user_session(user):
    user_session = db_name.Users.find_one(
        {"$and": [{"email": user["email"]}, {"status": "activate"}]})
    return JSONResponse(content={"user session": userEntityUpdate(user_session), "status": "Succes!"}, status_code=201)
