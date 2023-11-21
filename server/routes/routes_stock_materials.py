from fastapi import APIRouter, Depends
from utils.db import db_name
from bson import ObjectId
from schemas.schemas_stock_materials import rack_stock, racks_stock, stock_product, stocks_products, type_stock, types_stocks
from models.stock_materials_model import Floors, rackModel, Rows, SpaceRow, stock_products, typeStockModel, product_pieza
from controllers.warehouse_controller import create_warehouse_type, delete_warehouse_type, create_warehouse, delete_warehouse, create_rack, delete_rack, get_all_space_rack_status
from middlewares.warehouse_middleware import warehouse_exist, tpye_warehouse_exist, rack_exist, create_rack_validator

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


@stock_materials.post("/new_rack", tags=["Racks"], dependencies=[Depends(create_rack_validator)])
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


@stock_materials.get("/space_status", tags=["Racks"])
def get_all_space_rack_status_route(query_status: str = None, id_prod: str = None):
    return get_all_space_rack_status(query_status, id_prod)

# Prueba


@stock_materials.post("/new_pza")
def new_pza(pz: product_pieza):
    pieza = dict(pz)
    db_name.Product_Pza.insert_one(pieza)
    return {"status": "success!"}
