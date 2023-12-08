# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from models.recoleccion_model import Recoleccion, updaterecoleccion, ReceivedEmbark
from schemas.schema_recoleccion import recoleccionesEntity
# Middlewares
from middlewares.validate_Recoleccion_middleware import recoleccion_update_validator, recoleccion_validate_middleware
from middlewares.recoleccionExist_middleware import recoleccion_exist, num_ref_solicitud_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.recoleccion_controller import create_Recoleccion, get_Recolecciom, update_recoleccion, delete_recoleccion, receive_request_Logistics
recoleccion = APIRouter()




# Endppoints User Admin
@recoleccion.get("/admin/recoleccion", tags=["Recoleccion"], dependencies=[Depends(protectedAcountAdmin())])
async def find_all_user():
    return recoleccionesEntity(db_name.Recolections.find())


@recoleccion.get("/admin/recolecciones/{id}", tags=["Recoleccion"], dependencies=[Depends(recoleccion_exist), Depends(protectedAcountAdmin())])
async def find_product(id: str):
    return get_Recolecciom(id)



@recoleccion.put("/admin/admin/recoleccion/{id}", tags=["Recoleccion"], dependencies=[Depends(recoleccion_exist), Depends(protectedAcountAdmin())])
async def update_find__recoleccion(id: str):
    return update_recoleccion(id)


# Endpoint para recibir embarque enviado por proveedor


@recoleccion.post("/receive-embark", tags=["Embark"], dependencies=[Depends(num_ref_solicitud_exist)])
async def receive_embark_route(embark: ReceivedEmbark):
    list_mp_as_dict = [mp.dict() for mp in embark.list_Mp]
    # Crear un diccionario con los datos restantes
    data_to_insert = {
        "num_ref_solicitud": embark.num_ref_solicitud, "list_Mp": list_mp_as_dict}

    return receive_request_Logistics(data_to_insert)