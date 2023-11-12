from utils.db import db_name
from fastapi import Response
from schemas.schema_prducts import productEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


def create_prduct(product):
    new_product = dict(product)
    print(new_product)
    id = db_name.Products.insert_one(new_product).inserted_id
    user = db_name.Products.find_one({"_id": id})
    return productEntity(user)


def get_prduct(id):
    product = db_name.Products.find_one({"_id": ObjectId(id)})
    return productEntity(product)


def update_product(id, product):
    db_name.Products.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(db_name.Products.find_one({"_id": ObjectId(id)}))


def delete_product(id):
    db_name.Products.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
