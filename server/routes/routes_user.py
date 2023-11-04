from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_user import usersEntity
from models.user_model import User, updateUser, loginUser


# Middlewares
from middlewares.validate_user_middleware import user_validate_middleware, user_update_validator
from middlewares.userExist_middleware import account_exist, user_exist
from middlewares.auth_middleware import Portador, protectedAcountAdmin
# Controllers
from controllers.user_controller import create_user, get_user, update_user, delete_user, login
user = APIRouter()

# {
#   "email": "tier2@gmail.com",
#   "password": "tier21234"
# }

# Token


@user.post("/login")
def login_user(user: loginUser):
    return login(dict(user))


@user.get("/user_session")
def get_user_session(user: loginUser = Depends(Portador())):
    return user


@user.get("/users", dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
def find_all_user():
    return usersEntity(db_name.Users.find())


@user.post("/user", dependencies=[Depends(account_exist), Depends(user_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_user_route(user: User):
    return create_user(user)


@user.get("/users/{id}", dependencies=[Depends(user_exist), Depends(Portador()), Depends(protectedAcountAdmin)])
def find_user(id: str):
    return get_user(id)


@user.put("/user/{id}", dependencies=[Depends(user_exist), Depends(user_update_validator), Depends(Portador()), Depends(protectedAcountAdmin)])
def update_find__user(id: str, user: updateUser):
    return update_user(id, user)


@user.delete("/user/{id}", dependencies=[Depends(user_exist), Depends(Portador())])
def delete_find_user(id: str, user: loginUser = Depends(protectedAcountAdmin())):
    return delete_user(id, user)
