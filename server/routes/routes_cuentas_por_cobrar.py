# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from fastapi.responses import JSONResponse

from schemas.schema_cuentas_por_cobrar import cuentas_por_cobrarEntity
from models.cuentas_por_cobrar_model import Cuenta_por_cobrar, updateCuenta_por_cobrar
# Middlewares
from middlewares.validate_cuenta_por_cobrar_middleware import cuenta_por_cobrar_update_validator, ceuenta_por_cobrar_validate_middleware
from middlewares.CuentaPorCobrarExist_middleware import cuentas_por_cobrar_exist, valid_status
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuenta_por_cobrar_controller import create_cuenta_por_cobrar, get_cuenta_por_cobrar, update_cuenta_por_cobrar, delete_cuenta_por_cobrar
cuentacobrar = APIRouter()

# Endppoints User Clients


# Endppoints User Admin
@cuentacobrar.get("/cuentacobrar", tags=["Cuentas por cobrar"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
def find_all_admin():
    list_cuentas = db_name.CuentasPorCobrar.find()
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)


# @cuentacobrar.post("/cuentacobrar",  tags=["Cuentas por cobrar"], dependencies=[Depends(ceuenta_por_cobrar_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
# def create_product_route(cuenta, Cnta):
#     return create_cuenta_por_cobrar(cuenta)


@cuentacobrar.put("/cuentacobrar/{id}",  tags=["Cuentas por cobrar"], dependencies=[Depends(cuentas_por_cobrar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__ceuntacobrar(id: str):
    return update_cuenta_por_cobrar(id)


@cuentacobrar.get("/cuentascobrar/status", tags=["Cuentas por cobrar"], dependencies=[Depends(valid_status), Depends(Portador())])
def get_cuentas_cobrar_status(status: str):
    list_cuentas = db_name.CuentasPorCobrar.find({"status": status})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentas_por_cobrarEntity(list_cuentas)}, status_code=200)

# @cuentacobrar.delete("/cuentacobara/{id}",  tags=["Cuentas por cobrar"], dependencies=[Depends(cuentas_por_cobrar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
# def delete_find_ceuntapgar(id: str):
#     return delete_cuenta_por_cobrar(id)
