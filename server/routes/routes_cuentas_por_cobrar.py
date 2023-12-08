# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from fastapi.responses import JSONResponse

from schemas.schema_cuentas_por_cobrar import cuentas_por_cobrarEntity
# Middlewares
from middlewares.CuentaPorCobrarExist_middleware import cuentas_por_cobrar_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuenta_por_cobrar_controller import  update_cuenta_por_cobrar,get_cuentas_por_cobrar_month
cuentacobrar = APIRouter()

# Endppoints User Admin
@cuentacobrar.get("/admin/cuentacobrar", tags=["Accounts Receivable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="devuelve todas las cuentas por cobrar de todos los clientes")
async def find_all_admin():
    list_cuentas = db_name.CuentasPorCobrar.find()
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/admin/cuentacobrar/status/pending", tags=["Accounts Receivable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="devuelve todas las cuentas por cobrar en estado pendiente de todos los clientes")
async def find_pending_admin():
    list_cuentas = db_name.CuentasPorCobrar.find({"status":"pending"})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/admin/cuentacobrar/paid", tags=["Accounts Receivable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="devuelve todas las cuentas por cobrar en estado pagado de todos los clientes")
async def find_complete_admin():
    list_cuentas = db_name.CuentasPorCobrar.find({"status":"paid"})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/admin/cuentacobrar/date-month/{month}", tags=["Accounts Receivable"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())], description="devuelve todas las cuentas por cobrar de todos los clientes")
async def find_month_admin(month):
    return get_cuentas_por_cobrar_month(month, email =None)

# Endppoints User Client
@cuentacobrar.get("/cuentacobrar", tags=["Accounts Receivable"], description="devuelve todas las cuentas por pagar del cliente logeado")
async def find_all_client(user =Depends(Portador())):
    list_cuentas = db_name.CuentasPorCobrar.find({"Deudor":user["email"]})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/cuentacobrar/status/pending", tags=["Accounts Receivable"], description="devuelve  las cuentas por pagar en estado pendiente del cliente logeado")
async def find_pending_client(user =Depends(Portador())):
    list_cuentas = db_name.CuentasPorCobrar.find({"status":"pending","Deudor":user["email"]})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/cuentacobrar/status/paid", tags=["Accounts Receivable"],  description="devuelve las cuentas pagadas en estado completado del cliente logeado")
async def find_complete_client(user = Depends(Portador())):
    list_cuentas = db_name.CuentasPorCobrar.find({"status":"paid", "Deudor":user["email"]})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

@cuentacobrar.get("/cuentacobrar/date-month/{month}", tags=["Accounts Receivable"],  description="devuelve  las cuentas por pagar por mes del cliente logeado")
async def find_month_client(month, user =Depends(Portador())):
    return get_cuentas_por_cobrar_month(month, user["email"])


@cuentacobrar.put("/cuentacobrar/pay/{id}",  tags=["Accounts Receivable"], dependencies=[Depends(cuentas_por_cobrar_exist)], description="Actualiza el status a pagado, es decir cuando el ususario realiza el pago correspondiente")
async def update_ceuntacobrar(id: str, user = Depends(Portador())):
    return update_cuenta_por_cobrar(id, user["email"])


