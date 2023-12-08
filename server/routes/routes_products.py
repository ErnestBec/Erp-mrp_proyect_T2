# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_prducts import productsEntity,productsUserEntity
from models.prodcuts_model import Prducto, updatePrducto
# Middlewares
from middlewares.validate_product_middleware import product_update_validator, product_validate_middleware
from middlewares.productExist_middleware import product_exist
from middlewares.auth_middleware import protectedAcountAdmin, Portador
# Controllers
from controllers.product_controller import create_prduct, get_prduct, update_product, delete_product
product = APIRouter()


# Endppoints User Clients

@product.get("/products-user", tags=["Products"], dependencies=[Depends(Portador())])
def find_all_user():
    return productsUserEntity(db_name.Products.find())


@product.get("/products/{id}", tags=["Products"], dependencies=[Depends(product_exist), Depends(Portador())])
def find_product(id: str):
    return get_prduct(id)

# Endppoints User Admin


@product.get("/admin/products", tags=["Products"], dependencies=[Depends(Portador()), Depends(protectedAcountAdmin())])
def find_all_admin():
    return productsEntity(db_name.Products.find())


@product.post("/admin/product", tags=["Products"], dependencies=[Depends(product_validate_middleware), Depends(Portador()), Depends(protectedAcountAdmin())])
def create_product_route(producto: Prducto):
    return create_prduct(producto)


@product.put("/admin/products/{id}", tags=["Products"], dependencies=[Depends(product_exist), Depends(product_update_validator), Depends(Portador()), Depends(protectedAcountAdmin())])
def update_find__product(id: str, product: updatePrducto):
    return update_product(id, product)


