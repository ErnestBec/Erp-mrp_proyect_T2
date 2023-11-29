from utils.db import db_name
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.schema_stock_materials import stock_rackspace_Entity
from bson import ObjectId


def new_rackspace_product(stock):
    new_stock = dict(stock)
    new_stock["product_stored"] = ObjectId(new_stock["product_stored"])
    id = db_name.stock_products.insert_one(new_stock).inserted_id
    stock_inserted = db_name.stock_products.find_one({"_id": id})
    if stock_inserted == None:
        raise HTTPException(
            detail="Ocurrio un error al crear el almacen, intentelo mas tarde", status_code=500)
    return JSONResponse(content={"stackspace": stock_rackspace_Entity(stock_inserted), "status": "the rockspace insert correct"}, status_code=201)
