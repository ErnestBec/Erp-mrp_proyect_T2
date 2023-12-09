from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from utils.db import db_name
# Schemas
from schemas.business_rule_max_prod import busness_rules_schema
# Models
from models.business_rule_models import BusinnesRuleMaxProd
# Middlewares
from middlewares.auth_middleware import  protectedAcountAdmin
# Controllers
from controllers.business_rules_controller import new_business_rule_prod_capacity, update_busimess_rule_prod_capacity
# Routing request
routes_business_rules = APIRouter()


# Routes Business Rules Production Capacity

# New Business Rule Production Capacity
@routes_business_rules.post("/admin/new_rule/production_capacity", tags=["Petition Rules"], dependencies=[Depends(protectedAcountAdmin())])
def new_business_rule_prod_capacity_route(business_rule: BusinnesRuleMaxProd):
    return new_business_rule_prod_capacity(business_rule)

# Get Rule Production Capacity


@routes_business_rules.get("/admin/get_rule/production_capacity" , tags=["Petition Rules"], dependencies=[Depends(protectedAcountAdmin())])
def get_rule_prod_capacity_route():
    business_rule = db_name.BusinessRuleMaxProd.find()
    return JSONResponse(content={"Business Rules": busness_rules_schema(business_rule)}, status_code=200)


# Update Business Rule Production Capacity


@routes_business_rules.patch("/admin/update_rule/production_capacity" , tags=["Petition Rules"], dependencies=[Depends(protectedAcountAdmin())])
def update_rule_prod_capacity_route(business_rule: BusinnesRuleMaxProd):
    return update_busimess_rule_prod_capacity(business_rule)
