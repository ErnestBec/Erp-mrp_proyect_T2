# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_cuentas_por_cobrar import cuentas_por_cobrarEntity
from models.cuentas_por_cobrar_model import Cuenta_por_cobrar ,updateCuenta_por_cobrar
# Middlewares
from middlewares.validate_cuenta_por_cobrar_middleware import cuenta_por_cobrar_update_validator, ceuenta_por_cobrar_validate_middleware
from middlewares.CuentaPorCobrarExist_middleware import cuentas_por_cobrar_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.cuenta_por_cobrar_controller import create_cuenta_por_cobrar, get_cuenta_por_cobrar, update_cuenta_por_cobrar, delete_cuenta_por_cobrar
cuentacobrar = APIRouter()

# Endppoints User Clients


@cuentacobrar.get("/cuentacobrar", tags=["Client"], dependencies=[Depends(Portador())])
def find_all_user():
    return cuentas_por_cobrarEntity(db_name.CuentasPorCobrar.find().toArray())


@cuentacobrar.get("/cuentacobrar/{id}", tags=["Client"], dependencies=[Depends(cuentas_por_cobrar_exist), Depends(Portador())])
def find_product(id: str):
    return get_cuenta_por_cobrar(id)

# Endppoints User Admin
@cuentacobrar.get("/cuentacobrar", tags=["Admin"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def find_all_admin():
    return cuentas_por_cobrarEntity(db_name.CuentasPorCobrar.find().toArray())


@cuentacobrar.post("/cuentapagar", tags=["Admin"], dependencies=[Depends(ceuenta_por_cobrar_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_product_route(cuenta, Cnta):
    return create_cuenta_por_cobrar(cuenta)


@cuentacobrar.put("/cuentapagar/{id}", tags=["Admin"], dependencies=[Depends(cuentas_por_cobrar_exist), Depends(cuenta_por_cobrar_update_validator), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__ceuntacobrar(id: str, cuenta: updateCuenta_por_cobrar):
    return update_cuenta_por_cobrar(id, cuenta)


@cuentacobrar.delete("/products/{id}", tags=["Admin"], dependencies=[Depends(cuentas_por_cobrar_exist), Depends(Portador()), Depends(protectedAcountAdmin())])
def delete_find_product(id: str):
    return delete_cuenta_por_cobrar(id)
