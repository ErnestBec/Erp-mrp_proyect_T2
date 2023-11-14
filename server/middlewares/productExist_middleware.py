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
        product = db_name.Products.find_one(
            {"num_pieza": ref_product["product"]})
        product.pop("_id")
        product.pop("nam_prod")
        product.pop("Descripcion")
        product.pop("min_stock")
        product.pop("max_stock")
        product.pop("precio_uni")
        product.pop("num_pieza")
        product.pop("categoria_prod")
        product.pop("cantidad_prod")
        product.pop("mp")
    
        products.append(
            {ref_product["product"]: product, "quantyti": ref_product["quantity"]})
    return products

