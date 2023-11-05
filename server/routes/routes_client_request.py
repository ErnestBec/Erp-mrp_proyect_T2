from fastapi import APIRouter, Depends
from utils.db import db_name
# Schemas
from schemas.schema_client_request import requestsClientEntity
# Models
from models.requests_client_model import RequestsClient
from models.user_model import userSession
# Middlewares
from middlewares.auth_middleware import Portador, protectedAcountAdmin
# Controllers
from controllers.requests_client_controller import new_request
# routing requests
requests_client = APIRouter()


# Ruta para insercion automatica

@requests_client.post("/client/request/api", tags=["Client:API"])
def new_request_route(request: RequestsClient):
    return new_request(request)

# Routes for Client


@requests_client.post("/client/request", tags=["Client"], dependencies=[Depends(Portador())])
def new_request_route(request: RequestsClient):
    return new_request(request)


@requests_client.get("client/requests", tags=["Client"])
def get_all_request_route():
    return


@requests_client.get("/client/request/{status}", tags=["Client"])
def get_request_status_route():
    return


@requests_client.get("/client/request/{date}", tags=["Client"])
def get_request_date_route():
    return


# Routes for Admin
@requests_client.get("/admin/requests", tags=["Admin"])
def get_all_request_route():
    return


@requests_client.get("/admin/request/{status}", tags=["Admin"])
def get_request_status_route():
    return


@requests_client.get("/admin/request/{date}", tags=["Admin"])
def get_request_date_route():
    return


@requests_client.put("/admin/request/{id}", tags=["Admin"])
def update_status_request_route():
    return
