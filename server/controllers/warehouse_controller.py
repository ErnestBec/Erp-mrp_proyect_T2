from utils.db import db_name
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.schemas_stock_materials import floor_rack, floors_rack, rack_stock, racks_stock, row_rack, rows_rack, space_row, spaces_row, stock_product, stocks_products, type_stock, types_stocks
from middlewares.warehouse_middleware import is_valid_object_id


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
    new_rack = db_name.Racks.find_one({"_id": ObjectId(id)})
    new_rack["date_update"] = str(new_rack["date_update"])
    return JSONResponse(content={"warehouse_type": rack_stock(new_rack), "status": "Success!"}, status_code=201)


def delete_rack(id):
    db_name.Racks.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Floors


def create_floor(floor):
    new_floor = dict(floor)
    if not is_valid_object_id(new_floor["id_rack"]):
        raise HTTPException(
            status_code=400, detail="The id of rack invalid!")
    rack = db_name.Racks.find_one(
        {"_id": ObjectId(new_floor["id_rack"])})
    if not rack:
        raise HTTPException(
            status_code=404, detail="The rack doest not exist!")
    floors_used = db_name.Floors.count_documents(
        {"id_rack": str(rack["_id"])})
    print(floors_used)
    if floors_used >= rack["high_capacity"]:
        raise HTTPException(
            detail="The selected rack does not have more floors available", status_code=404)
    id = db_name.Floors.insert_one(new_floor).inserted_id
    new_floor = db_name.Floors.find_one({"_id": ObjectId(id)})
    return JSONResponse(content={"warehouse_type": floor_rack(new_floor), "status": "Success!"}, status_code=201)


def delete_floor(id):
    db_name.Floors.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Rows


def create_row(row):
    new_row = dict(row)
    if not is_valid_object_id(new_row["id_floor"]):
        raise HTTPException(
            status_code=400, detail="The id of floor invalid!")
    floor = db_name.Floors.find_one(
        {"_id": ObjectId(new_row["id_floor"])})
    if not floor:
        raise HTTPException(
            status_code=404, detail="The floor doest not exist!")
    rack = db_name.Racks.find_one({"_id": ObjectId(floor["id_rack"])})
    rows_used = db_name.Rows.count_documents(
        {"id_floor": str(floor["_id"])})
    print(floor["_id"])
    if rows_used >= rack["width_capacity"]:
        raise HTTPException(
            detail="The selected floor does not have more rows available", status_code=404)
    id = db_name.Rows.insert_one(new_row).inserted_id
    new_row = db_name.Rows.find_one({"_id": ObjectId(id)})
    return JSONResponse(content={"warehouse_type": row_rack(new_row), "status": "Success!"}, status_code=201)


def delete_row(id):
    db_name.Rows.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# controllers space rows


def create_space_row(space_row_req):
    new_space_row = dict(space_row_req)
    if not is_valid_object_id(new_space_row["id_row"]):
        raise HTTPException(
            status_code=400, detail="The id of row invalid!")
    row = db_name.Rows.find_one(
        {"_id": ObjectId(new_space_row["id_row"])})
    if not row:
        raise HTTPException(
            status_code=404, detail="The row doest not exist!")
    floor = db_name.Floors.find_one({"_id": ObjectId(row["id_floor"])})
    print(floor)
    rack = db_name.Racks.find_one({"_id": ObjectId(floor["id_rack"])})
    print(rack)
    space_rows_used = db_name.SpaceRow.count_documents(
        {"id_row": str(row["_id"])})
    print(space_rows_used)
    if space_rows_used >= rack["long_capacity"]:
        raise HTTPException(
            detail="The selected space row does not have more rows available", status_code=404)
    id = db_name.SpaceRow.insert_one(new_space_row).inserted_id
    new_space_row = db_name.SpaceRow.find_one({"_id": ObjectId(id)})
    return JSONResponse(content={"warehouse_type": space_row(new_space_row), "status": "Success!"}, status_code=201)


def delete_space_row(id):
    db_name.SpaceRow.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)
