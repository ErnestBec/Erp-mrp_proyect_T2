from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def rowMaterial_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The Raw Material doest not exist!")
    user = db_name.RawMaterials.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="Thw RawMaterials pagar doest not exist!")

    return request


def RawMaterial_ref(ref: list):
    rammaterial = []
    for ref_rawmate in ref:
        raw= db_name.RawMaterials.find_one(
            {"status": ref_rawmate["status"]})
        raw.pop("_id")
        raw.pop("fecha")
        raw.pop("lugar")
        raw.pop("id_cobro")
        raw.pop("status")
    
        rammaterial.append(
            {ref_rawmate["fecha"]: raw, "lugar": ref_rawmate["lugar"]})
    return rammaterial

