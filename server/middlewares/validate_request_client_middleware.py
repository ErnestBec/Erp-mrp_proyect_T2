from fastapi import Request, HTTPException
from middlewares.userExist_middleware import user_email
from utils.db import db_name
from bson import ObjectId


async def request_client_validate_middleware(request: Request):
    errors = []
    request_client = await request.json()
    if not request_client["client"]:
        errors.append("The client cannot be empty")
    user_req = user_email(request_client["client"])
    if user_req == None:
        errors.append("The entered user is not registred as a customer!")
    if not request_client["products"]:
        errors.append("The products cannot be empty")
    err_prduct = validate_products(request_client["products"])
    if err_prduct:
        errors.append(err_prduct)
    if not request_client["date_delivery_expected"]:
        errors.append("The date_delivery_expected cannot be empty")

    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


def validate_products(products: list):
    for ref_product in products:
        if not is_valid_object_id(ref_product["id_pro"]):

            return f"The product with id: {ref_product['id_pro']}doest not exist!"

        product = db_name.Products.find_one(
            {"_id": ObjectId(ref_product["id_pro"])})
        if not product:
            return "The product doest not exist!"
