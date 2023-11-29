# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
# Models
from models.stock_materials_model import RackSpace
# Controllers
from controllers.stocks_controller import new_rackspace_product
# Schemas
from schemas.schema_stock_materials import stocks_spacesRacks_Entity
stocks = APIRouter()


# Endpoints RackSpace


@stocks.post("/newrackspace")
def new_rackspace_route(stock: RackSpace):
    return new_rackspace_product(stock)


@stocks.get("/racksspaces")
def get_all_racksSpace():
    return stocks_spacesRacks_Entity(db_name.stock_products.find())
