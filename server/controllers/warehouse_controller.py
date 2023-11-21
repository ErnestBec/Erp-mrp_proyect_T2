from utils.db import db_name
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.schemas_stock_materials import rack_stock, stock_product, type_stock, spaces_row
from middlewares.warehouse_middleware import is_valid_object_id
from datetime import datetime, timedelta


def create_warehouse_type(warehouse_type):
    new_warehouse_type = dict(warehouse_type)
    id = db_name.TypeWarehouse.insert_one(new_warehouse_type).inserted_id
    warehouse_type = db_name.TypeWarehouse.find_one({"_id": id})
    return JSONResponse(content={"warehouse_type": type_stock(warehouse_type), "status": "Success!"}, status_code=201)


def delete_warehouse_type(id):
    db_name.TypeWarehouse.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Warehouse


def create_warehouse(warehouse):
    new_warehouse = dict(warehouse)
    if not is_valid_object_id(new_warehouse["id_type_stock"]):
        raise HTTPException(
            status_code=400, detail="The id of type of warehouse invalid!")
    type_warehouse = db_name.TypeWarehouse.find_one(
        {"_id": ObjectId(new_warehouse["id_type_stock"])})
    if not type_warehouse:
        raise HTTPException(
            status_code=404, detail="The type warehouse doest not exist!")
    id = db_name.Warehouse.insert_one(new_warehouse).inserted_id
    new_warehouse = db_name.Warehouse.find_one({"_id": ObjectId(id)})
    new_warehouse["date_update"] = str(new_warehouse["date_update"])
    return JSONResponse(content={"warehouse_type": stock_product(new_warehouse), "status": "Success!"}, status_code=201)


def delete_warehouse(id):
    db_name.Warehouse.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Racks


def create_rack(rack):
    new_rack = dict(rack)
    if not is_valid_object_id(new_rack["id_stock"]):
        raise HTTPException(
            status_code=400, detail="The id of warehouse invalid!")
    warehouse = db_name.Warehouse.find_one(
        {"_id": ObjectId(new_rack["id_stock"])})
    if not warehouse:
        raise HTTPException(
            status_code=404, detail="The warehouse doest not exist!")
    id = db_name.Racks.insert_one(new_rack).inserted_id
    for i in range(0, new_rack["high_capacity"]):
        create_floor(
            {"id_rack": id, "long": new_rack["long_capacity"], "width_capacity": new_rack["width_capacity"]})
    new_rack = db_name.Racks.find_one({"_id": ObjectId(id)})
    new_rack["date_update"] = str(new_rack["date_update"])
    return JSONResponse(content={"warehouse_type": rack_stock(new_rack), "status": "Success!"}, status_code=201)


def delete_rack(id):
    db_name.Racks.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Floors


def create_floor(floor):
    new_floor = dict(floor)
    id = db_name.Floors.insert_one(
        {"id_rack": new_floor["id_rack"]}).inserted_id
    for i in range(0, new_floor["long"]):
        create_row(
            {"id_floor": id, "width_capacity": new_floor["width_capacity"]})
    new_floor = db_name.Floors.find_one({"_id": ObjectId(id)})


def create_row(row):
    new_row = dict(row)
    id = db_name.Rows.insert_one({"id_floor": new_row["id_floor"]}).inserted_id
    for i in range(0, new_row["width_capacity"]):
        create_space_row({"id_row": id})
    new_row = db_name.Rows.find_one({"_id": ObjectId(id)})


def create_space_row(space_row_req):
    new_space_row = dict(space_row_req)
    id = db_name.SpaceRow.insert_one(
        {"id_row": new_space_row["id_row"], "id_prod": "Null", "status": "free"}).inserted_id
    new_space_row = db_name.SpaceRow.find_one({"_id": ObjectId(id)})
    print(new_space_row)


def verified_almacen(products):
    request_production = []
    for product in products:
        product = dict(product)
        products_pzs = db_name.Product_Pza.count_documents(
            {"$and": [{"id_product": product["id_pro"]}, {"status": "active"}]})
        if int(product["quantity"]) > products_pzs:
            print("No alcanta el producto:")
            quantity_missing = product["quantity"]-products_pzs
            request_production.append(
                {"id_prod": product["id_pro"], "quantity_missing": quantity_missing})
        else:
            "Hola"
    if len(request_production) == 0:
        return datetime.now().strftime("%d-%m-%y")
    else:
        # Realizar peticion de produccion
        fecha_actual = datetime.now()
        nuevos_dias = 5
        nueva_fecha = fecha_actual + timedelta(days=nuevos_dias)
        return nueva_fecha.strftime("%d-%m-%y")


def get_all_space_rack_status(query_status, id_prod):
    if not is_valid_object_id(id_prod):
        raise HTTPException(
            status_code=400, detail="The id of tipe of rack invalid!")
    spaces = db_name.SpaceRow.find(
        {"$and": [{"status": query_status}, {"id_prod": id_prod}]})

    return {"status": spaces_row(spaces)}
