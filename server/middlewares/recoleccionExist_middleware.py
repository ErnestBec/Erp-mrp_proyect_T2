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


def num_ref_solicitud_exist(embark=Body(...)):
    embark = dict(embark)
    num_ref_solicitud = embark["num_ref_solicitud"]
    reques_exist = db_name.Request_Supplier.find_one(
        {"$and": [{"num_ref_request": num_ref_solicitud}, {"status": "pending"}]})
    if not reques_exist:
        raise HTTPException(
            status_code=404, detail="The number reference request doest not exist or is it already completed!")
    if len(embark["list_Mp"]) != len(reques_exist["list_mp"]):
        raise HTTPException(
            status_code=404, detail=f"The number of pieces does not correspond to what was requested, They left {len(embark["list_Mp"])} pieces and we requested {len(reques_exist["list_mp"])}")
    list_mp_embar = list(embark["list_Mp"])
    list_mp_request = reques_exist["list_mp"]
    for mp_emnark in embark["list_Mp"]:
        mp_request = next(
            (obj for obj in list_mp_request if obj["id_mp"]
             == mp_emnark["id_mp"]),
            None
        )
        if (mp_request is None):
            raise HTTPException(
                detail="La mp no corresponde a la solicictada", status_code=404)
        print(mp_emnark["quantity"])
        print(mp_request["order_quantity"])
        if mp_emnark["quantity"] != mp_request["order_quantity"]:
            raise HTTPException(
                detail="La cantidad no corresponde a la solicictada", status_code=404)
    return embark


def recoleccion_ref(ref: list):
    recoleccion = []
    for ref_reco in ref:
        reco = db_name.Recolecciones.find_one(
            {"status": ref_reco["status"]})
        reco.pop("_id")
        reco.pop("fecha")
        reco.pop("lugar")
        reco.pop("id_cobro")
        reco.pop("status")

        recoleccion.append(
            {ref_reco["fecha"]: reco, "lugar": ref_reco["lugar"]})
    return recoleccion
