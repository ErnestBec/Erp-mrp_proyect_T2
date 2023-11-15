# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_recoleccion import recoleccionesEntity
from models.recoleccion_model import Recoleccion,updaterecoleccion
# Middlewares
from middlewares.validate_Recoleccion_middleware import recoleccion_update_validator, recoleccion_validate_middleware
from middlewares.recoleccionExist_middleware import recoleccion_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.recoleccion_controller import create_Recoleccion, get_Recolecciom, update_recoleccion, delete_recoleccion
recoleccion = APIRouter()

# Endppoints User Clients


@recoleccion.get("/recoleccion", tags=["Client"], dependencies=[Depends(Portador())])
def find_all_user():
    return recoleccionesEntity(db_name.Recolecciones.find().toArray())


@recoleccion.get("/recolecciones/{id}", tags=["Client"], dependencies=[Depends(recoleccion_exist), Depends(Portador())])
def find_product(id: str):
    return get_Recolecciom(id)

# Endppoints User Admin
@recoleccion.get("/recolecion", tags=["Admin"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def find_all_admin():
    return recoleccionesEntity(db_name.Recolecciones.find().toArray())


@recoleccion.post("/recolecciones", tags=["Admin"], dependencies=[Depends(recoleccion_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_recoleccion_route(recoleccio: Recoleccion):
    return create_Recoleccion(recoleccio)


@recoleccion.put("/recoleccion/{id}", tags=["Admin"], dependencies=[Depends(recoleccion_exist), Depends(recoleccion_update_validator), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__recoleccion(id: str, reco: updaterecoleccion):
    return update_recoleccion(id, reco)


@recoleccion.delete("/recoleccion/{id}", tags=["Admin"], dependencies=[Depends(recoleccion_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def delete_find_recoleccion(id: str):
    return delete_recoleccion(id)
