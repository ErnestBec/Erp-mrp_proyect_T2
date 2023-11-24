from utils.db import db_name
from fastapi import Response, HTTPException
from fastapi.responses import JSONResponse
from schemas.schema_prducts import productEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from middlewares.warehouse_middleware import is_valid_object_id


def create_prduct(product):
    new_product = dict(product)
    i = 0
    for mp in new_product["mp"]:
        if not is_valid_object_id(mp.id_mp):
            raise HTTPException(
                status_code=400, detail="The id of raw material is invalid!")
        mp = db_name.RawMaterials.find_one({"_id": ObjectId(mp.id_mp)})
        if not mp:
            raise HTTPException(
                status_code=404, detail="The raw material doest not exist!")

        new_product["mp"][i] = dict(new_product["mp"][i])
        i = +1
    id = db_name.Products.insert_one(new_product).inserted_id
    product = db_name.Products.find_one({"_id": id})
    return JSONResponse(content={"product": productEntity(product), "status": "Success!"}, status_code=201)


def get_prduct(id):
    product = db_name.Products.find_one({"_id": ObjectId(id)})
    return productEntity(product)


def update_product(id, product):
    db_name.Products.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(db_name.Products.find_one({"_id": ObjectId(id)}))


def delete_product(id):
    # db_name.Products.find_one({"_id": ObjectId(id)})
    # db_name.SpaceRow.find_one_and_update({"_id": ObjectId(product["id_space_stock"])}, {
    #                                      "$set": {"status": "free"}})
    db_name.Products.find_one_and_delete(
        {"_id": ObjectId(id)})

    return Response(status_code=HTTP_204_NO_CONTENT)
