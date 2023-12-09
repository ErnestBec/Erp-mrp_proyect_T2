# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_orden_produccion import Ordenes_ProduccionEntity
# Middlewares
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.orden_produccion_controller import get_order_production_month
OrdenProducc = APIRouter()

# Endppoints User Admin


@OrdenProducc.get("/admin/order-production", tags=["Orden de Produccion"], dependencies=[Depends(protectedAcountAdmin())], description="Devuelve todas las ordenes de produccion echas, acceso solo admin")
async def find_all_admin_orders():
    return Ordenes_ProduccionEntity(db_name.OrderProduction.find())

@OrdenProducc.get("/admin/order-production/status/pending", tags=["Orden de Produccion"], dependencies=[Depends(protectedAcountAdmin())], description="Devuelve todas las ordenes de produccion en estado pendiente, acceso solo admin")
async def find_pendindg_admin_orders():
    return Ordenes_ProduccionEntity(db_name.OrderProduction.find({"status":"pending"}))

@OrdenProducc.get("/admin/order-production/status/complete", tags=["Orden de Produccion"], dependencies=[Depends(protectedAcountAdmin())], description="Devuelve todas las ordenes de produccion en estado completado, solo acceso admin")
async def find_complete_admin_orders():
    return Ordenes_ProduccionEntity(db_name.OrderProduction.find({"status":"complete"}))

@OrdenProducc.get("/admin/order-production/date-mounth/{month}", tags=["Orden de Produccion"], dependencies=[Depends(protectedAcountAdmin())], description="Devuelve todas las ordenes de produccion por mes indicado en numero es decir Enero = 01, solo acceso admin")
async def find_month_admin_orders(month:int):
    return get_order_production_month(month)

