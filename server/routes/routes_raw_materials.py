from fastapi import APIRouter, Depends
from controllers.row_materials_controller import create_rawMaterial
from models.raw_materials_model import raw_materials

raw_material = APIRouter()


@raw_material.post("/rawmaterial")
def new_raw_material_route(raw_material: raw_materials):
    return create_rawMaterial(raw_material)


@raw_material.get("/rawmaterials")
def get_all_raw_materials_route():
    return


@raw_material.get("/rawmaterial/{id}")
def get_raw_material_route(id):
    return


@raw_material.put("/rawmaterial/{id}")
def update_raw_material_route(id):
    return


@raw_material.delete("/rawmaterial/{id}")
def delete_raw_material_route(id):
    return
