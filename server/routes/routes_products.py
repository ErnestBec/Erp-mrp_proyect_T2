
from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schema_prducts import productsEntity
from models.prodcuts_model import Prducto, updatePrducto


# Middlewares
from middlewares.validate_product_middleware import product_update_validator,product_validate_middleware
from middlewares.productExist_middleware import product_exist
# Controllers
from controllers.product_controller import create_prduct, get_prduct, update_product, delete_product
product = APIRouter()


@product.get("/product")
def find_all_user():
    return productsEntity(db_name.Products.find())


@product.post("/product", dependencies=[Depends(product_validate_middleware)])
def create_product_route(producto: Prducto):
    return create_prduct(product)


@product.get("/products/{id}", dependencies=[Depends(product_exist)])
def find_product(id: str):
    return get_prduct(id)


@product.put("/products/{id}", dependencies=[Depends(product_exist), Depends(product_update_validator)])
def update_find__product(id: str, product: updatePrducto):
    return update_product(id, product)


@product.delete("/products/{id}", dependencies=[Depends(product_exist)])
def delete_find_product(id: str):
    return delete_product(id)
