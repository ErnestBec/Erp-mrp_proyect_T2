from fastapi import APIRouter, Depends, Query
from utils.db import db_name
from starlette.requests import Request
# Schemas
from schemas.schema_client_request import requestsClientEntity
# Models
from models.requests_client_model import RequestsClient
from models.user_model import userSession
# Middlewares
from middlewares.auth_middleware import Portador, protectedAcountAdmin
from middlewares.request_client_middleware import exist_request_client
from middlewares.validate_request_client_middleware import request_client_validate_middleware
from middlewares.userExist_middleware import is_valid_object_id
# Controllers
from controllers.requests_client_controller import new_request, get_request_month
# routing requests
requests_client = APIRouter()



# Routes Admin


@requests_client.get("/admin/requests", tags=["Requests"], dependencies=[Depends(protectedAcountAdmin()),Depends(Portador())],description="Devuelve todas las solicitudes de los clientes solo con acceso Admin")
async def get_all_request_route_admin():
    return requestsClientEntity(db_name.Request_Client.find())

@requests_client.get("/admin/requests/status/pending", tags=["Requests"], dependencies=[Depends(protectedAcountAdmin()),Depends(Portador())],description="Devuelve las solicitudes en estado pendiente de todos los clientes solo con acceso Admin")
async def get_all_pending_request_route_admin():
    return requestsClientEntity(db_name.Request_Client.find({"status":"pending"}))

@requests_client.get("/admin/requests/status/complete", tags=["Requests"], dependencies=[Depends(protectedAcountAdmin()),Depends(Portador())],description="Devuelve las solicitudes en estado completado  de todos los clientes solo con acceso Admin")
async def get_all_complete_request_route_admin():
    return requestsClientEntity(db_name.Request_Client.find({"status":"complete"}))

@requests_client.get("/admin/requests/date-mont/{month}", tags=["Requests"], dependencies=[Depends(protectedAcountAdmin()),Depends(Portador())],description="Devuelve las solicitudes por mes  de todos los clientes solo con acceso Admin")
async def get_all_month_request_route_admin(month):
    return get_request_month(month, email =None)


# Routes for Client

@requests_client.get("/requests", tags=["Requests"] , description="Devuelve todas las solicitudes del usuario logeado")
async def get_all_request_status_route_client(user = Depends(Portador())):
    return requestsClientEntity(db_name.Request_Client.find({"client.email":user["email"]}))

@requests_client.get("/requests/status/pending", tags=["Requests"] , description="Devuelve las solicitudes en estado pendiente del usuario logeado")
async def get_all_pending_request_status_route_client(user = Depends(Portador())):
    return requestsClientEntity(db_name.Request_Client.find({"status": "pending","client.email":user["email"]}))

@requests_client.get("/requests/status/complete", tags=["Requests"] , description="Devuelve las solicictudes en estado completado del usuario logeado")
async def get_all_complete_request_status_route_client(user = Depends(Portador())):
    return requestsClientEntity(db_name.Request_Client.find({"status": "complete","client.email":user["email"]}))


@requests_client.get("/request/date-mont/{month}", tags=["Requests"], description="Devuelve todas las solicitudes por mes del ususario logeado")
async def get_all_month_request_date_route_client(month:int,user = Depends(Portador()) ):
    return get_request_month(month, user["email"])

# Ruta para insercion automatica

@requests_client.post("/client/request/api", tags=["Requests"], dependencies=[Depends(request_client_validate_middleware)],description="Endpoint con el que se generarran las peticiones de clientes")
async def new_request_route_client(request: RequestsClient, user=Depends(Portador())):
    return new_request(request, user)


