from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def recoleccion_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The recollecion doest not exist!")
    user = db_name.Recolecciones.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The cuenta por pagar doest not exist!")

    return request


def recoleccion_ref(ref: list):
    recoleccion = []
    for ref_reco in ref:
        reco= db_name.Recolecciones.find_one(
            {"status": ref_reco["status"]})
        reco.pop("_id")
        reco.pop("fecha")
        reco.pop("lugar")
        reco.pop("id_cobro")
        reco.pop("status")
    
        recoleccion.append(
            {ref_reco["fecha"]: reco, "lugar": ref_reco["lugar"]})
    return recoleccion

