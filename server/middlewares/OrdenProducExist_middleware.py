from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def orden_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The order doest not exist!")
    user = db_name.OrdenesProduccion.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The product doest not exist!")

    return request


def ordenProd_ref(ref: list):
    ordenes = []
    for ref_orden in ref:
        ordenes = db_name.OrdenesProduccion.find_one(
            {"producto": ref_orden["fecha_alta"]})
        ordenes.pop("_id")
        ordenes.pop("fecha_alta")
        ordenes.pop("solicitud")
        ordenes.pop("producto")
        ordenes.pop("cantidad_fabri")
        ordenes.pop("id_pieza")
    
        ordenes.append(
            {ref_orden["producto"]: ordenes})
    return ordenes

