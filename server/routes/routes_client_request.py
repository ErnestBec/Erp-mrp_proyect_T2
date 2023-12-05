from fastapi import APIRouter, Depends
from utils.db import db_name
# Schemas
from schemas.schema_client_request import requestsClientEntity
# Models
from models.requests_client_model import RequestsClient
from models.user_model import userSession
# Middlewares
from middlewares.auth_middleware import Portador, protectedAcountAdmin
from middlewares.request_client_middleware import exist_request_client
from middlewares.validate_request_client_middleware import request_client_validate_middleware
# Controllers
from controllers.requests_client_controller import new_request, get_request_month
# routing requests
requests_client = APIRouter()


# Ruta para insercion automatica

@requests_client.post("/client/request/api", tags=["Client:API"], dependencies=[Depends(Portador())])
def new_request_route(request: RequestsClient):
    return new_request(request)

# Routes for Client


@requests_client.post("/client/request", tags=["Client"], dependencies=[Depends(Portador()), Depends(exist_request_client)])
def new_request_route(request: RequestsClient):
    return new_request(request)

# Routes generales


@requests_client.get("/requests", tags=["Client-Admin"], dependencies=[Depends(Portador())])
def get_all_request_route():
    return requestsClientEntity(db_name.Request_Client.find())


@requests_client.get("/request/status/{status}", tags=["Client-Admin"], dependencies=[Depends(Portador())])
def get_request_status_route(status: str):
    return requestsClientEntity(db_name.Request_Client.find({"status": status}))


@requests_client.get("/request/date/{month}", tags=["Client-Admin"], description="The month must be written in English and the first letter in capital letters", dependencies=[Depends(Portador())])
def get_request_date_route(month: str):
    return get_request_month(month)


# Routes for Admin

@requests_client.put("/admin/request/{id}", tags=["Admin"])
def update_status_request_route():
    return
