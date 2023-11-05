from fastapi import APIRouter, Depends


raw_material = APIRouter()


@raw_material.post("/rawmaterial")
def new_raw_material_route():
    return


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
