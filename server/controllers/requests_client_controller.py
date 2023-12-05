from utils.db import db_name
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException
import calendar
import random
from datetime import datetime, date
# Schemas
from schemas.schema_client_request import requestClientEntity, requestsClientEntity, requestClientEntityInser
# Middleware
from middlewares.userExist_middleware import user_email
from middlewares.productExist_middleware import product_ref
from bson import ObjectId
# Controllers
from controllers.warehouse_controller import verified_almacen
from controllers.cuenta_por_cobrar_controller import create_cuenta_por_cobrar

# _id: Optional[str]
# status: Optional[str] = "pending"
# client: dict
# date_req: Optional[str]
# products: List[products]
# num_ref_solicitud: Optional[str]
# date_approved: Optional[str]
# date_delivery_expected: Optional[str]
# date_delivery: Optional[str]


def new_request(request):
    data_request = dict(request)
    date_request = datetime.now()
    print(data_request)
    response_client = {}
    data_request["num_ref_solicitud"] = generate_num_ref(
        data_request["client"])
    # Validamos Almacen de materias terminadas
    data_request["date_delivery"] = verified_almacen(
        data_request["products"], data_request["num_ref_solicitud"])

    user_req = user_email(data_request["client"])
    data_request["client"] = user_req
    data_request["products"] = product_ref(data_request["products"])
    date_request = date_request.strftime("%d-%m-%y")
    data_request["date_approved"] = datetime.now().strftime("%d-%m-%y")
    data_request.update({"date_req": date_request})
    data_request.update({"status": "pending"})
    id = db_name.Request_Client.insert_one(data_request).inserted_id
    request_inserted = db_name.Request_Client.find_one({"_id": id})
    # Integramos la respuesta del cliente
    response_client["num_ref_solicitud"] = data_request["num_ref_solicitud"]
    importe = generate_total_cost(data_request["products"])
    response_client["importe"] = importe
    response_client["date_approved"] = data_request["date_approved"]
    response_client["date_delivery"] = data_request["date_delivery"]
    # Ingresamos a cuentas por cobrar
    create_cuenta_por_cobrar(
        {"id_request": id, "importe": importe, "date_issue": date_request, "date_pay": None})
    # Validad Capacidad de Produccion

    return JSONResponse(content={"request": response_client, "status": "Success!"}, status_code=201)


def request_raw_materials():
    return ""


def get_request_month(month):
    data = db_name.Request_Client.find()
    list_request = []
    for request in list(data):
        dia, mes, año = map(int, request["date_req"].split("-"))
        nombre_mes = calendar.month_name[mes]
        if month == nombre_mes:
            list_request.append(request)

    return JSONResponse(content={"requests": requestsClientEntity(list_request), "status": "Succes!"}, status_code=201)


def generate_num_ref(email):
    num_ref = email[:3]+date.today().strftime("%Y%m%d") + \
        str(random.randint(1, 100))
    return num_ref


def generate_total_cost(products):
    list(products)
    total_cost = 0
    for product in products:
        cost_product = product["product"]
        total_cost = int(cost_product["precio_uni"]
                         * product["quantyti"])+total_cost
    return total_cost
