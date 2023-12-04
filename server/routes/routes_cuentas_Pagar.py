# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_cuentas_pagar import cuentasPagarEntity
from fastapi.responses import JSONResponse
# Middlewares
from middlewares.validate_cuentaPagar_middleware import cuenta_Pagar_update_validator, ceuenta_Pagar_validate_middleware
from middlewares.CuentaPagarrExist_middleware import cuentas_Pagar_exist
from middlewares.CuentaPorCobrarExist_middleware import valid_status
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuentaPagar_controller import create_cuentaPagar, get_cuentaPagar, delete_cuentaPagar, update_cuentaPagar

cuentaPagar = APIRouter()

# Endppoints User Clients


# Endppoints User Admin
@cuentaPagar.get("/cuentapagar", tags=["Cuentas Por Pagar"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
def find_all_admin():
    list_cuentas_pagar = db_name.CuentasPagar.find()
    list_cuentas_pagar = list(list_cuentas_pagar)
    return cuentasPagarEntity(list_cuentas_pagar)


# @cuentaPagar.post("/cuentapagar",  tags=["Cuentas Por Pagar"], dependencies=[Depends(ceuenta_Pagar_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
# def create_cuentaPagar(cuenta, CntaP):
#     return create_cuentaPagar(cuenta)


@cuentaPagar.put("/cuentapagar/{id}", tags=["Cuentas Por Pagar"], dependencies=[Depends(cuentas_Pagar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__cuentaPagar(id: str):
    return update_cuentaPagar(id)


@cuentaPagar.get("/cuentaspagar/status", tags=["Cuentas Por Pagar"], dependencies=[Depends(valid_status), Depends(Portador())])
def get_cuentas_cobrar_status(status: str):
    list_cuentas = db_name.CuentasPorPagar.find({"status": status})
    list_cuentas = list(list_cuentas)
    return JSONResponse(content={"all_acounts": cuentasPagarEntity(list_cuentas)}, status_code=200)

# @cuentaPagar.delete("/cuentapagar/{id}",  tags=["Cuentas Por Pagar"], dependencies=[Depends(cuentas_Pagar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
# def delete_find_cuentaPagar(id: str):
#     return delete_cuentaPagar(id)
