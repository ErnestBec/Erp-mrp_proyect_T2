from utils.db import db_name
from fastapi import Response
from schemas.raw_materials import raw_materials
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_rawMaterial(raw):
    new_rawmat = dict(raw)
    id = db_name.RawMaterials.insert_one(new_rawmat).inserted_id
    cuenta = db_name.RawMaterials.find_one({"_id": id})
    return raw_materials(cuenta)


def get_rawMaterial(id):
    rawmat = db_name.RawMaterials.find_one({"_id": ObjectId(id)})
    return raw_materials(rawmat)


def update_rawMaterial(id, raw):
    db_name.RawMaterials.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(raw)})
    return raw_materials(db_name.RawMaterials.find_one({"_id": ObjectId(id)}))


def delete_rawMaterial(id):
    db_name.RawMaterials.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
