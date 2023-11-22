from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_cuentaPagart_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def cuentas_Pagar_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_cuentaPagart_id(id):
        raise HTTPException(
            status_code=400, detail="The cuenta por pagar doest not exist!")
    user = db_name.CuentasPorPagar.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The cuenta por pagar doest not exist!")

    return request


