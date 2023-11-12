# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_orden_produccion import Ordenes_ProduccionEntity
from models.orden_produccion_model import Orden_Produccion, updateorden_Prduccion
# Middlewares
from middlewares.validate_OrderProd_middleware import OrdenProducc_update_validator, OrdenProd_validate_middleware
from middlewares.OrdenProducExist_middleware import orden_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.orden_produccion_controller import create_orden_produccion, get_Orden_produccion, update_Orden_prooduccion, delete_Orden_Produccion
OrdenProducc = APIRouter()

# Endppoints User Admin
@OrdenProducc.get("/ordenproduc", tags=["Admin"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def find_all_admin_orders():
    return Ordenes_ProduccionEntity(db_name.OrdenesProduccion.find().toArray())


@OrdenProducc.post("/orderp", tags=["Admin"], dependencies=[Depends(OrdenProd_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_product_route(order: Orden_Produccion):
    return create_orden_produccion(order)


@OrdenProducc.put("/orderpro/{id}", tags=["Admin"], dependencies=[Depends(orden_exist), Depends(OrdenProducc_update_validator), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__Orders(id: str, order: updateorden_Prduccion):
    return update_Orden_prooduccion(id, order)


@OrdenProducc.delete("/orderdel/{id}", tags=["Admin"], dependencies=[Depends(orden_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def delete_find_orders(id: str):
    return delete_Orden_Produccion(id)
