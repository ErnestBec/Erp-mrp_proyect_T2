from utils.db import db_name
from fastapi.responses import JSONResponse
import calendar
from datetime import datetime
# Schemas
from schemas.schema_client_request import requestClientEntity, requestsClientEntity, requestClientEntityInser
# Middleware
from middlewares.userExist_middleware import user_email
from middlewares.productExist_middleware import product_ref


def new_request(request):
    data_request = dict(request)
    date_request = datetime.now()
    data_request["client"] = user_email(data_request["client"])
    data_request["products"] = product_ref(data_request["products"])
    date_request = date_request.strftime("%d-%m-%y")
    data_request.update({"date_req": date_request})
    data_request.update({"date_approved": ""})
    data_request.update({"date_delivery_expected": ""})
    data_request.update({"date_delivery": ""})
    id = db_name.Request_Client.insert_one(data_request).inserted_id
    request_inserted = db_name.Request_Client.find_one({"_id": id})
    return JSONResponse(content={"request": requestClientEntity(request_inserted), "status": "Success!"}, status_code=201)


def verified_almacen():
    return


def get_request_month(month):

    data = db_name.Request_Client.find()
    list_request = []
    for request in list(data):
        dia, mes, año = map(int, request["date_req"].split("-"))
        nombre_mes = calendar.month_name[mes]
        if month == nombre_mes:
            list_request.append(request)

    return JSONResponse(content={"requests": requestsClientEntity(list_request), "status": "Succes!"}, status_code=201)
