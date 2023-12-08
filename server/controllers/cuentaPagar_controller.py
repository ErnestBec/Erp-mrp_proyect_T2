from utils.db import db_name
from schemas.schema_cuentas_pagar import cuentaPagarEntity,cuentasPagarEntity
from bson import ObjectId
from fastapi.responses import JSONResponse
from datetime import datetime


def create_cuentaPagar(ctpa):
    new_cuenta_pagar = dict(ctpa)
    id = db_name.CuentasPorPagar.insert_one(new_cuenta_pagar).inserted_id
    cuenta = db_name.CuentasPorPagar.find_one({"_id": id})


def get_cuentaPagar(id):
    cuentap = db_name.CuentasPorPagar.find_one({"_id": ObjectId(id)})
    return cuentaPagarEntity(cuentap)


def update_cuentaPagar(id):
    db_name.CuentasPorPagar.update_one(
        {"_id": ObjectId(id)}, {"$set": {"status": "paid"}})
    cuenta_update = db_name.CuentasPorPagar.find_one({"_id": ObjectId(id)})
    cuenta_update = dict(cuenta_update)
    return cuentaPagarEntity(cuenta_update)


def get_cuentas_por_pagar_month(month,email):
    if email == None :
        data = db_name.CuentasPorPagar.find()
    else:
        data = db_name.CuentasPorPagar.find({"Acreedor":email})
    list_acount = []
    for request in list(data):
        fecha = datetime.strptime(request["date_registration"], "%Y-%m-%d %H:%M:%S")
        mes = fecha.month
        if int(month) == int(mes):
            list_acount.append(request)

    return JSONResponse(content={"requests": cuentasPagarEntity(list_acount), "status": "Succes!"}, status_code=201)
