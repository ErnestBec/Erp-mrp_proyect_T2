# libreries
from fastapi import APIRouter, Depends
from utils.db import db_name
# Models
from models.request_supply_model import RequestSupply
# Controllers
from controllers.request_supply_controller import create_request_supply


request_Supply = APIRouter()


@request_Supply.post("/entry-to-warehouse")
def entry_to_warehouse(request_supply: RequestSupply):
    return create_request_supply(request_supplier=request_Supply)


@request_Supply.get("/request-supply")
def get_all_request_supply():
    return
