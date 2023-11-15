from utils.db import db_name
from fastapi import Response, HTTPException
from schemas.schema_prducts import productEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from middlewares.warehouse_middleware import is_valid_object_id


def create_prduct(product):
    new_product = dict(product)
    if not is_valid_object_id(new_product["id_space_stock"]):
        raise HTTPException(
            status_code=400, detail="The id of space row invalid!")
    space_stock = db_name.SpaceRow.find_one(
        {"_id": ObjectId(new_product["id_space_stock"])})
    if not space_stock:
        raise HTTPException(
            status_code=404, detail="The space row doest not exist!")
    if space_stock["status"] != "free":
        raise HTTPException(
            detail="the space selected it is used!", status_code=401)
    id = db_name.Products.insert_one(new_product).inserted_id
    user = db_name.Products.find_one({"_id": id})
    db_name.SpaceRow.find_one_and_update({"_id": space_stock["_id"]}, {
                                         "$set": {"status": "used"}})
    return productEntity(user)


def get_prduct(id):
    product = db_name.Products.find_one({"_id": ObjectId(id)})
    return productEntity(product)


def update_product(id, product):
    db_name.Products.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(db_name.Products.find_one({"_id": ObjectId(id)}))


def delete_product(id):
    product = db_name.Products.find_one({"_id": ObjectId(id)})
    db_name.SpaceRow.find_one_and_update({"_id": ObjectId(product["id_space_stock"])}, {
                                         "$set": {"status": "free"}})
    db_name.Products.find_one_and_delete(
        {"_id": ObjectId(id)})

    return Response(status_code=HTTP_204_NO_CONTENT)
