from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_user import usersEntity, userEntityUpdate
from models.user_model import User, updateUser, loginUser


# Middlewares
from middlewares.validate_user_middleware import user_validate_middleware, user_update_validator
from middlewares.userExist_middleware import account_exist, user_exist
from middlewares.auth_middleware import Portador, protectedAcountAdmin
# Controllers
from controllers.user_controller import create_user, get_user, update_user, delete_user, login, get_user_session
# nicializamos rutas
user = APIRouter()

# {
#   "email": "tier2@gmail.com",
#   "password": "tier21234"
# }

# Token


@user.post("/login", tags=["Users"])
def login_user(user: loginUser):
    return login(dict(user))


@user.get("/user_session", tags=["Users"])
def get_user_session_route(user: loginUser = Depends(Portador())):
    return get_user_session(user)


@user.put("/admin/user/{id}", tags=["Users"], dependencies=[Depends(user_exist), Depends(user_update_validator), Depends(protectedAcountAdmin())])
def update_find__user(id: str, user: updateUser, userSession=Depends(Portador())):
    return update_user(id, dict(user), userSession)

# Routes for Administrators


@user.get("/users", tags=["Users"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
def find_all_user():
    return usersEntity(db_name.Users.find())


@user.post("/admin/user", tags=["Users"], dependencies=[Depends(account_exist), Depends(user_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_user_route(user: User):
    return create_user(user)


@user.get("/admin/user/{id}", tags=["Users"], dependencies=[Depends(user_exist), Depends(Portador()), Depends(protectedAcountAdmin)])
def find_user(id: str):
    return get_user(id)


@user.delete("/admin/user/{id}", tags=["Users"], dependencies=[Depends(user_exist), Depends(Portador())])
def delete_find_user(id: str, user: loginUser = Depends(protectedAcountAdmin())):
    return delete_user(id, user)
