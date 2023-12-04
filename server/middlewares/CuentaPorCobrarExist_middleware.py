from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId
from fastapi.params import Body


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def cuentas_por_cobrar_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The cuenta por pagar doest not exist!")
    user = db_name.CuentasPorCobrar.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The cuenta por pagar doest not exist!")

    return request


def valid_status(request: Request):
    status = request.query_params.get("status")
    print(status)
    if status == "pending":
        return request
    elif status == "paid":
        return request
    raise HTTPException(
        status_code=404, detail="the status invalid, pending or paid ")


def cuentacobrar_ref(ref: list):
    cuentas = []
    for ref_cuentas in ref:
        cuenta = db_name.CuentasPorCobrar.find_one(
            {"importe": ref_cuentas["cuenta"]})
        cuenta.pop("_id")
        cuenta.pop("solicitud")
        cuenta.pop("importe")
        cuenta.pop("fecha_emision")
        cuenta.pop("total")
        cuenta.pop("fecha_de_pago")

        cuentas.append(
            {ref_cuentas["solictud"]: cuenta, "total": ref_cuentas["total"]})
    return cuentas
