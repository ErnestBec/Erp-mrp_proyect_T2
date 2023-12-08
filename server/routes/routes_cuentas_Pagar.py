# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_cuentas_pagar import cuentasPagarEntity
from fastapi.responses import JSONResponse
# Middlewares
from middlewares.CuentaPagarrExist_middleware import cuentas_Pagar_exist
from middlewares.CuentaPorCobrarExist_middleware import valid_status
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuentaPagar_controller import  update_cuentaPagar,get_cuentas_por_pagar_month

cuentaPagar = APIRouter()


# Endppoints User Admin
@cuentaPagar.get("/admin/cuentapagar", tags=["Acount Payable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="Devuelve todas las cuentas por pagar, solo Acceso Admin")
async def find_all_acount_payable_admin():
    list_cuentas_pagar = db_name.CuentasPorPagar.find()
    list_cuentas_pagar = list(list_cuentas_pagar)
    return cuentasPagarEntity(list_cuentas_pagar)

@cuentaPagar.get("/admin/cuentapagar/status/pending", tags=["Acount Payable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())],description="Devuelve todas las cuentas pendientes por pagar, solo Acceso Admin")
async def find_all_account_payable_pending_admin():
    list_cuentas_pagar = db_name.CuentasPorPagar.find({"status":"pending"})
    list_cuentas_pagar = list(list_cuentas_pagar)
    return cuentasPagarEntity(list_cuentas_pagar)

@cuentaPagar.get("/admin/cuentapagar/status/paid", tags=["Acount Payable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())],description="Devuelve todas las cuentas pagadas, solo Acceso Admin")
async def find_all_account_payable_paid_admin():
    list_cuentas_pagar = db_name.CuentasPorPagar.find({"status":"paid"})
    list_cuentas_pagar = list(list_cuentas_pagar)
    return cuentasPagarEntity(list_cuentas_pagar)

@cuentaPagar.get("/admin/cuentapagar/date-month/{month}", tags=["Acount Payable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())],description="Devuelve todas las cuentas por pagar filtradas por meses, solo Acceso Admin")
async def find_all_admin(month:int):
    return get_cuentas_por_pagar_month(month, email=None)

@cuentaPagar.put("/cuentapagar/{id}", tags=["Acount Payable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin()),Depends(cuentas_Pagar_exist) ],description="Actualiza el estado a pagado, es decir se hace el pago correspondiente, solo Acceso Admin")
async def update_find__cuentaPagar(id: str):
    return update_cuentaPagar(id)

