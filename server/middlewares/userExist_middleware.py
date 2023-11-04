from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


async def account_exist(request: Request):
    user = await request.json()

    user_exist = db_name.Users.find_one({"email": user["email"]})
    if user_exist:
        raise HTTPException(
            status_code=409, detail="There is already an account associated with this email")


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def user_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The user doest not exist!")
    user = db_name.Users.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The user doest not exist!")

    return request
