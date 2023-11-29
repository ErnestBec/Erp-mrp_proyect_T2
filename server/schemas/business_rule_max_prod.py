def business_rule_schema(business_rule) -> dict:
    return {
        "_id": str(business_rule["_id"]),
        "max_pro": business_rule["max_prod"],
        "min_prod": business_rule["min_prod"]
    }


def busness_rules_schema(business_rules) -> list:
    return [business_rule_schema(rule) for rule in business_rules]
