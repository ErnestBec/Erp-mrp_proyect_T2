from utils.db import db_name
from fastapi import Response
from schemas.schema_orden_produccion import orden_produccionEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_orden_produccion(orden):
    new_orden = dict(orden)
    id = db_name.OrdenesProduccion.insert_one(new_orden).inserted_id
    ord = db_name.OrdenesProduccion.find_one({"_id": id})
    return orden_produccionEntity(ord)


def get_Orden_produccion(id):
    orden = db_name.OrdenesProduccion.find_one({"_id": ObjectId(id)})
    return orden_produccionEntity(orden)


def update_Orden_prooduccion(id, orden):
    db_name.OrdenesProduccion.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(orden)})
    return orden_produccionEntity(db_name.OrdenesProduccion.find_one({"_id": ObjectId(id)}))


def delete_Orden_Produccion(id):
    db_name.OrdenesProduccion.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
