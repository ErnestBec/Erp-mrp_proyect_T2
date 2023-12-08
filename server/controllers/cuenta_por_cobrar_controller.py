from utils.db import db_name
from schemas.schema_cuentas_por_cobrar import cuenta_por_cobrarEntity,cuentas_por_cobrarEntity
from bson import ObjectId
from fastapi.responses import JSONResponse
from datetime import datetime


def create_cuenta_por_cobrar(ctc):
    new_cuenta_Cobrar = dict(ctc)
    id = db_name.CuentasPorCobrar.insert_one(new_cuenta_Cobrar).inserted_id
    cuenta = db_name.CuentasPorCobrar.find_one({"_id": id})

    if not cuenta:
        return False
    else:
        return True



def update_cuenta_por_cobrar(id,email):
    db_name.CuentasPorCobrar.update_one(
        {"_id": ObjectId(id), "Deudor":email}, {"$set": {"status": "paid"}})
    cuenta = db_name.CuentasPorCobrar.find_one({"_id": ObjectId(id)})
    print(cuenta)
    return JSONResponse(content={"update_acount": cuenta_por_cobrarEntity(cuenta)}, status_code=200)


def get_cuentas_por_cobrar_month(month,email):
    if email == None :
        data = db_name.CuentasPorCobrar.find()
    else:
        data = db_name.CuentasPorCobrar.find({"Deudor":email})
    list_acount = []
    for request in list(data):
        fecha = datetime.strptime(request["date_registration"], "%Y-%m-%d %H:%M:%S")
        mes = fecha.month
        if int(month) == int(mes):
            list_acount.append(request)

    return JSONResponse(content={"requests": cuentas_por_cobrarEntity(list_acount), "status": "Succes!"}, status_code=201)
