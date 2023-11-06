from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def exist_request_client(num_ref_solicitud):
    request = db_name.Request_Client.find_one(
        {"num_ref_solicitud": num_ref_solicitud})
    if request != None:
        raise HTTPException(
            detail=f"Ya existe una solicitud con referencia: '{num_ref_solicitud}', no puede modificar la solicitud!", status_code=400)
    return
