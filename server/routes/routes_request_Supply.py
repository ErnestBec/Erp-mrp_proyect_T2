# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
# Schemas
from schemas.request_suppply_schema import requests_supply_schema
# Controllers
from controllers.request_supply_controller import get_request_supplier_month
# Middlewares
from middlewares.auth_middleware import Portador, protectedAcountAdmin

request_Supply = APIRouter()


@request_Supply.get("/admin/request-supplier" , tags=["Request Supplier"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())],description="Devuelve las peticiones al proveedor, acceso solo admin")
def get_all_request_supplier():
    list_request_supplier = db_name.Request_Supplier.find()
    return requests_supply_schema(list_request_supplier)


@request_Supply.get("/admin/request-supply/status/pending", tags=["Request Supplier"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="Devuelve las peticiones al proveedor en estado pendiente, acceso solo admin")
def get_all_request_supply_pending():
    list_request_supplier = db_name.Request_Supplier.find({"status":"pending"})
    return requests_supply_schema(list_request_supplier)

@request_Supply.get("/admin/request-supply/status/complete", tags=["Request Supplier"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="Devuelve las peticiones al proveedor en estado completado, acceso solo admin")
def get_all_request_supply_complete():
    list_request_supplier = db_name.Request_Supplier.find({"status":"complete"})
    return requests_supply_schema(list_request_supplier)

@request_Supply.get("/admin/request-supplier/date-month/{month}",  tags=["Request Supplier"],dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="Devuelve las peticiones al proveedor en estado completado, acceso solo admin")
async def get_request_supplier_month_route(month:int):
    return get_request_supplier_month(month)

@request_Supply.get("/admin/request-supplier/num-ref-sol/{num_ref}",  tags=["Request Supplier"],dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="Devuelve las peticiones al proveedor en estado completado, acceso solo admin")
async def get_request_supplier_month_route(num_ref:str):
    list_request_supplier = db_name.Request_Supplier.find({"num_ref_request":num_ref})
    return requests_supply_schema(list_request_supplier)