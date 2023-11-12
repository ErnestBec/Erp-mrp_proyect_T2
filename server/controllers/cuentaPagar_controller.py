from utils.db import db_name
from fastapi import Response
from schemas.schema_cuentas_pagar import cuentaPagarEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_cuentaPagar(ctpa):
    new_cuenta_pagar = dict(ctpa)
    id = db_name.CuentasPorPagar.insert_one(new_cuenta_pagar).inserted_id
    cuenta = db_name.CuentasPorPagar.find_one({"_id": id})
    return cuentaPagarEntity(cuenta)


def get_cuentaPagar(id):
    cuentap = db_name.CuentasPorPagar.find_one({"_id": ObjectId(id)})
    return cuentaPagarEntity(cuentap)


def update_cuentaPagar(id, cuentap):
    db_name.CuentasPorPagar.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(cuentap)})
    return cuentaPagarEntity(db_name.CuentasPorPagar.find_one({"_id": ObjectId(id)}))


def delete_cuentaPagar(id):
    db_name.CuentasPorPagar.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
