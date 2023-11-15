from utils.db import db_name
from fastapi import Request, HTTPException
from bson import ObjectId


def is_valid_object_id(id_str):
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False


async def tpye_warehouse_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The id of type of warehouse invalid!")
    user = db_name.TypeWarehouse.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The type warehouse materials doest not exist!")


async def warehouse_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="")
    user = db_name.Warehouse.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The warehouse materials doest not exist!")


async def rack_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The id of rack invalid!")
    user = db_name.Racks.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=404, detail="The rack doest not exist!")


async def floor_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The id of floor invalid!")
    floor = db_name.Floors.find_one({"_id": ObjectId(id)})
    if not floor:
        raise HTTPException(
            status_code=404, detail="The floor doest not exist!")


async def row_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The id of row invalid!")
    row = db_name.Rows.find_one({"_id": ObjectId(id)})
    if not row:
        raise HTTPException(
            status_code=404, detail="The row doest not exist!")


async def space_row_exist(req: Request):
    id = req.path_params.get("id")
    if not is_valid_object_id(id):
        raise HTTPException(
            status_code=400, detail="The id of space row invalid!")
    space_row = db_name.SpaceRow.find_one({"_id": ObjectId(id)})
    print(space_row)
    if not space_row:
        raise HTTPException(
            status_code=404, detail="The space row doest not exist!")
