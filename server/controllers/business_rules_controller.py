from utils.db import db_name
from fastapi.responses import JSONResponse
from bson import ObjectId
#
from schemas.business_rule_max_prod import business_rule_schema,  busness_rules_schema


def new_business_rule_prod_capacity(business_rule):
    business_rule = dict(business_rule)
    count_business_rule = db_name.BusinessRuleMaxProd.find()
    count_business_rule = list(count_business_rule)
    if len(count_business_rule) > 0:
        return JSONResponse(content={
            "error": "An active production rule exists, you cannot add another"}, status_code=400)
    id = db_name.BusinessRuleMaxProd.insert_one(business_rule).inserted_id
    new_business_rule = db_name.BusinessRuleMaxProd.find_one(
        {"_id": ObjectId(id)})
    return JSONResponse(content={"Business rule": business_rule_schema(new_business_rule), "status": "Success!"}, status_code=201)


def update_busimess_rule_prod_capacity(business_rule):
    business_rule = dict(business_rule)
    business_rule_all = db_name.BusinessRuleMaxProd.find()
    business_rule_arr = busness_rules_schema(business_rule_all)
    business_rulese_one = business_rule_arr[0]
    db_name.BusinessRuleMaxProd.update_one(
        {"_id": ObjectId(business_rulese_one["_id"])}, {"$set": business_rule})
    business_rule_all = db_name.BusinessRuleMaxProd.find()
    return JSONResponse(content={"Business Rule :": busness_rules_schema(business_rule_all)}, status_code=200)
