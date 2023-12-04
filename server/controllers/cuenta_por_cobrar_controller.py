from utils.db import db_name
from fastapi import Response
from schemas.schema_cuentas_por_cobrar import cuenta_por_cobrarEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.responses import JSONResponse


def create_cuenta_por_cobrar(ctc):
    new_cuenta_Cobrar = dict(ctc)
    id = db_name.CuentasPorCobrar.insert_one(new_cuenta_Cobrar).inserted_id
    cuenta = db_name.CuentasPorCobrar.find_one({"_id": id})

    if not cuenta:
        return False
    else:
        return True


def get_cuenta_por_cobrar(id):
    cuenta = db_name.CuentasPorCobrar.find_one({"_id": ObjectId(id)})
    return JSONResponse(content={"all_acounts": cuenta_por_cobrarEntity(cuenta)}, status_code=200)


def update_cuenta_por_cobrar(id):
    db_name.CuentasPorCobrar.update_one(
        {"_id": ObjectId(id)}, {"$set": {"status": "paid"}})
    cuenta = db_name.CuentasPorCobrar.find_one({"_id": ObjectId(id)})
    print(cuenta)
    return JSONResponse(content={"update_acount": cuenta_por_cobrarEntity(cuenta)}, status_code=200)


def delete_cuenta_por_cobrar(id):
    db_name.CuentasPorCobrar.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
