# Libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from bson import ObjectId
# Schemas
from schemas.schemas_stock_materials import rack_stock, racks_stock, stock_product, stocks_products, type_stock, types_stocks, spaces_row
# Models
from models.stock_materials_model import Floors, rackModel, Rows, SpaceRow, stock_products, typeStockModel, product_pieza
# Controllers
from controllers.warehouse_controller import create_warehouse_type,get_warehouse_capacity, create_warehouse, delete_warehouse, create_rack, delete_rack, get_all_space_rack_status
# Middlewares
from middlewares.warehouse_middleware import warehouse_exist, tpye_warehouse_exist, rack_exist, create_rack_validator
from middlewares.auth_middleware import protectedAcountAdmin


stock_materials = APIRouter()

# Routes for type Stock

@stock_materials.post("/admin/type_warehouse_materials/", tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin())], description="Ingresar un nuevo tipo de Almacen, solo acceso Admin")
async def warehouse_type(warehouse_type: typeStockModel):
    return create_warehouse_type(warehouse_type)


@stock_materials.get("/admin/type_warehouse_materials", tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin())], description="Mustra todos los tipos de almacen registrados, acceso solo admin")
async def get_all_types_warehouse():
    return types_stocks(db_name.TypeWarehouse.find())


@stock_materials.post("/admin/new_warehouse", tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin())], description="Ingresar un nuevo Almacen, solo acceso admin")
async def create_warehouse_route(warehouse: stock_products):
    return create_warehouse(warehouse)

@stock_materials.get("/admin/warehouse_materials", tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin())], description="Muestra todos los almacenes registrados, solo acceso admin")
async def get_all_types_warehouse():
    return stocks_products(db_name.Warehouse.find())

@stock_materials.get("/admin/warehouse-capacity/{id}" , tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin()),Depends(tpye_warehouse_exist)], description="Devuelve la capacidad de los almacenes, acceso solo admin")
async def get_warehouse_capacity_route(id:str):
    return get_warehouse_capacity(id)

# Routes Racks


@stock_materials.post("/admin/new_rack", tags=["Warehouse"], dependencies=[Depends(create_rack_validator),Depends(protectedAcountAdmin())],  description="Ingresa un nuevo rack a un almacen, solo acceso Admin")
async def create_rack_route(rack: rackModel):
    return create_rack(rack)


@stock_materials.get("/admin/racks", tags=["Warehouse"], dependencies=[Depends(protectedAcountAdmin())], description="Muestra todos los racks por almacen, solo acceso Admin")
async def get_all_racks():
    return racks_stock(db_name.Racks.find())


# @stock_materials.get("/rack/{id}", tags=["Racks"], dependencies=[Depends(rack_exist)])
# def get_rack_by_id(id):
#     return rack_stock(db_name.Racks.find_one({"_id": ObjectId(id)}))


# @stock_materials.get("/space_status", tags=["Racks"])
# def get_all_space_rack_status_route(query_status: str = None, id_prod: str = None):
#     return get_all_space_rack_status(query_status, id_prod)


@stock_materials.post("/new_pza", tags=["Warehouse"])
async def new_pza(pz: product_pieza):
    pieza = dict(pz)
    db_name.Product_Pza.insert_one(pieza)
    return {"status": "success!"}


@stock_materials.get("/space_row", tags=["Warehouse"])
async def get_all_space():
    all_spaces = db_name.SpaceRow.find()
    spaces = {}

    return spaces_row(all_spaces)
