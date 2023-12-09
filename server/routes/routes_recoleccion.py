# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from models.recoleccion_model import  ReceivedEmbark
from schemas.schema_recoleccion import recoleccionesEntity
# Middlewares
from middlewares.recoleccionExist_middleware import recoleccion_exist, num_ref_solicitud_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.recoleccion_controller import  get_Recolecciom, receive_request_Logistics
recoleccion = APIRouter()




# Endppoints User Admin
@recoleccion.get("/admin/recoleccion", tags=["Recoleccion"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
async def find_all_user():
    return recoleccionesEntity(db_name.Recolections.find())


@recoleccion.get("/admin/recolecciones/{id}", tags=["Recoleccion"], dependencies=[Depends(recoleccion_exist),Depends(Portador()), Depends(protectedAcountAdmin())])
async def find_product(id: str):
    return get_Recolecciom(id)
@recoleccion.get("/admin/recoleccion/num--ref-sol{num_ref}", tags=["Recoleccion"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
async def find_all_user(num_ref):
    return recoleccionesEntity(db_name.Recolections.find({"num_ref_solicictud":num_ref}))


# Endpoint para recibir embarque enviado por proveedor


@recoleccion.post("/receive-embark", tags=["Embark"], dependencies=[Depends(num_ref_solicitud_exist)])
async def receive_embark_route(embark: ReceivedEmbark):
    list_mp_as_dict = [mp.dict() for mp in embark.list_Mp]
    # Crear un diccionario con los datos restantes
    data_to_insert = {
        "num_ref_solicitud": embark.num_ref_solicitud, "list_Mp": list_mp_as_dict}

    return receive_request_Logistics(data_to_insert)