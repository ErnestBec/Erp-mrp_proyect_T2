# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_cuentas_pagar import cuentasPagarEntity

# Middlewares
from middlewares.validate_cuentaPagar_middleware import cuenta_Pagar_update_validator, ceuenta_Pagar_validate_middleware
from middlewares.CuentaPagarrExist_middleware import cuentas_Pagar_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuentaPagar_controller import create_cuentaPagar,get_cuentaPagar, delete_cuentaPagar, update_cuentaPagar

cuentaPagar = APIRouter()

# Endppoints User Clients


# Endppoints User Admin
@cuentaPagar.get("/cuentapagar", tags=["Cuentas Por Pagar"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def find_all_admin():
    return cuentasPagarEntity(db_name.CuentasPorPagar.find().toArray())


@cuentaPagar.post("/cuentapagar",  tags=["Cuentas Por Pagar"], dependencies=[Depends(ceuenta_Pagar_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_cuentaPagar(cuenta, CntaP):
    return create_cuentaPagar(cuenta)



@cuentaPagar.put("/cuentapagar/{id}", tags=["Cuentas Por Pagar"], dependencies=[Depends(cuentas_Pagar_exist), Depends(cuenta_Pagar_update_validator), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__cuentaPagar(id: str, cuenta: update_cuentaPagar):
    return update_cuentaPagar(id, cuenta)


@cuentaPagar.delete("/cuentapagar/{id}",  tags=["Cuentas Por Pagar"], dependencies=[Depends(cuentas_Pagar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def delete_find_cuentaPagar(id: str):
    return delete_cuentaPagar(id)
