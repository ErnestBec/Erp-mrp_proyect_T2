from fastapi import APIRouter, Depends
from controllers.row_materials_controller import create_rawMaterial
from models.raw_materials_model import raw_materials
from schemas.raw_materials import raws_materials
from utils.db import db_name
# Middlewares
from middlewares.validate_rawMateriasl_middleware import RowMaterial_validate_middleware
from middlewares.auth_middleware import protectedAcountAdmin, Portador
raw_material = APIRouter()

# enpoints de Admin


@raw_material.post("/rawmaterial", tags=["RowMaterials"], dependencies=[Depends(RowMaterial_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
async def new_raw_material_route(raw_material: raw_materials):
    return create_rawMaterial(raw_material)


@raw_material.get("/rawmaterials", tags=["RowMaterials"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
async def get_all_raw_materials_route():
    raw_materials = db_name.RawMaterials.find()
    raw_materials = list(raw_materials)
    return raws_materials(raw_materials)

