from fastapi import APIRouter, Depends
from utils.db import db_name
from bson import ObjectId
from schemas.schemas_stock_materials import floor_rack, floors_rack, rack_stock, racks_stock, row_rack, rows_rack, space_row, spaces_row, stock_product, stocks_products, type_stock, types_stocks
from models.stock_materials_model import Floors, rackModel, Rows, SpaceRow, stock_products, typeStockModel
from controllers.warehouse_controller import create_warehouse_type, delete_warehouse_type, create_warehouse, delete_warehouse, create_rack, delete_rack, create_floor, delete_floor, create_row, delete_row, create_space_row, delete_space_row
from middlewares.warehouse_middleware import warehouse_exist, tpye_warehouse_exist, rack_exist, floor_exist, row_exist, space_row_exist
stock_materials = APIRouter()

# Routes for type Stock


@stock_materials.post("/type_warehouse_materials/", tags=["Type Warehouse"])
def warehouse_type(warehouse_type: typeStockModel):
    return create_warehouse_type(warehouse_type)


@stock_materials.delete("/type_warehouse_materials/{id}", tags=["Type Warehouse"], dependencies=[Depends(tpye_warehouse_exist)])
def delete_warehouse_type_roue(id):
    return delete_warehouse_type(id)


@stock_materials.get("/type_warehouse_materials", tags=["Type Warehouse"])
def get_all_types_warehouse():
    return types_stocks(db_name.TypeWarehouse.find())


@stock_materials.get("/type_warehouse_materials/{id}", tags=["Type Warehouse"], dependencies=[Depends(tpye_warehouse_exist)])
def get_warehouse_type_by_id(id):
    return type_stock(db_name.TypeWarehouse.find_one({"_id": ObjectId(id)}))

# Routes warehouse


@stock_materials.post("/new_warehouse", tags=["Warehouse"])
def create_warehouse_route(warehouse: stock_products):
    return create_warehouse(warehouse)


@stock_materials.delete("/new_warehouse/{id}", tags=["Warehouse"], dependencies=[Depends(warehouse_exist)])
def delete_warehouse_route(id):
    return delete_warehouse(id)


@stock_materials.get("/warehouse_materials", tags=["Warehouse"])
def get_all_types_warehouse():
    return stocks_products(db_name.Warehouse.find())


@stock_materials.get("/warehouse_materials/{id}", tags=["Warehouse"], dependencies=[Depends(warehouse_exist)])
def get_warehouse_type_by_id(id):
    return stock_product(db_name.Warehouse.find_one({"_id": ObjectId(id)}))

# Routes Racks


@stock_materials.post("/new_rack", tags=["Racks"])
def create_rack_route(rack: rackModel):
    return create_rack(rack)


@stock_materials.delete("/rack/{id}", tags=["Racks"], dependencies=[Depends(rack_exist)])
def delete_rack_route(id):
    return delete_rack(id)


@stock_materials.get("/racks", tags=["Racks"])
def get_all_racks():
    return racks_stock(db_name.Racks.find())


@stock_materials.get("/rack/{id}", tags=["Racks"], dependencies=[Depends(rack_exist)])
def get_rack_by_id(id):
    return rack_stock(db_name.Racks.find_one({"_id": ObjectId(id)}))

# Routes Floors


@stock_materials.post("/new_floor", tags=["Floors"])
def create_rack_route(floor: Floors):
    return create_floor(floor)


@stock_materials.delete("/floor/{id}", tags=["Floors"], dependencies=[Depends(floor_exist)])
def delete_floor_route(id):
    return delete_floor(id)


@stock_materials.get("/floors", tags=["Floors"])
def get_all_floors():
    return floors_rack(db_name.Floors.find())


@stock_materials.get("/floor/{id}", tags=["Floors"], dependencies=[Depends(floor_exist)])
def get_floor_by_id(id):
    return floor_rack(db_name.Floors.find_one({"_id": ObjectId(id)}))

# Routes Rows


@stock_materials.post("/new_row", tags=["Rows"])
def create_row_route(row: Rows):
    return create_row(row)


@stock_materials.delete("/row/{id}", tags=["Rows"], dependencies=[Depends(row_exist)])
def delete_row_route(id):
    return delete_row(id)


@stock_materials.get("/rows", tags=["Rows"])
def get_all_row():
    return rows_rack(db_name.Rows.find())


@stock_materials.get("/row/{id}", tags=["Rows"], dependencies=[Depends(row_exist)])
def get_row_by_id(id):
    return row_rack(db_name.Rows.find_one({"_id": ObjectId(id)}))

# Routes Space Rows


@stock_materials.post("/new_space_row", tags=["Space Row"])
def create_space_row_route(space_row: SpaceRow):
    return create_space_row(space_row)


@stock_materials.delete("/space_row/{id}", tags=["Space Row"], dependencies=[Depends(space_row_exist)])
def delete_space_row_route(id):
    return delete_space_row(id)


@stock_materials.get("/space_rows", tags=["Space Row"])
def get_all_space_row():
    return spaces_row(db_name.SpaceRow.find())


@stock_materials.get("/space_row/{id}", tags=["Space Row"], dependencies=[Depends(space_row_exist)])
def get_space_row_by_id(id):
    return space_row(db_name.SpaceRow.find_one({"_id": ObjectId(id)}))
