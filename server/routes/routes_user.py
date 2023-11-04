
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_user import usersEntity
from models.user_model import User, updateUser


# Middlewares
from middlewares.validate_user_middleware import user_validate_middleware, user_update_validator
from middlewares.userExist_middleware import account_exist, user_exist
# Controllers
from controllers.user_controller import create_user, get_user, update_user, delete_user
user = APIRouter()


@user.get("/users")
def find_all_user():
    return usersEntity(db_name.Users.find())


@user.post("/user", dependencies=[Depends(account_exist), Depends(user_validate_middleware)])
def create_user_route(user: User):
    return create_user(user)


@user.get("/users/{id}", dependencies=[Depends(user_exist)])
def find_user(id: str):
    return get_user(id)


@user.put("/users/{id}", dependencies=[Depends(user_exist), Depends(user_update_validator)])
def update_find__user(id: str, user: updateUser):
    return update_user(id, user)


@user.delete("/users/{id}", dependencies=[Depends(user_exist)])
def delete_find_user(id: str):
    return delete_user(id)
