from utils.db import db_name
from fastapi import Response
from schemas.schema_recoleccion import recoleccionEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_Recoleccion(recoleccion):
    new_recoleccion = dict(recoleccion)
    id = db_name.Recolecciones.insert_one(new_recoleccion).inserted_id
    recol = db_name.Recolecciones.find_one({"_id": id})
    return recoleccionEntity(recol)


def get_Recolecciom(id):
    product = db_name.Recolecciones.find_one({"_id": ObjectId(id)})
    return recoleccionEntity(product)


def update_recoleccion(id, recoleccion):
    db_name.Recolecciones.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(recoleccion)})
    return recoleccionEntity(db_name.Recolecciones.find_one({"_id": ObjectId(id)}))


def delete_recoleccion(id):
    db_name.Recolecciones.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
