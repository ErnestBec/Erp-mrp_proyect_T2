from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def product_exist(request: Request):
    id = request.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The product doest not exist!")
    user = db_name.Products.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The product doest not exist!")

    return request


def product_ref(ref: list):
    products = []
    for ref_product in ref:
        ref_product = dict(ref_product)
        if not is_valid_object_id(ref_product["id_pro"]):
            raise HTTPException(
                status_code=400, detail="The product doest not exist!")
        product = db_name.Products.find_one(
            {"_id": ObjectId(ref_product["id_pro"])}, {"name_prod": 1, "_id": 1, "precio_uni": 1})
        product["_id"] = str(product["_id"])
        products.append(
            {"product": product, "quantyti": ref_product["quantity"]})
    return products
