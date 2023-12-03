def request_supply_schema(request_supply) -> dict:
    return {
        "_id": str(request_supply["_id"]),
        "list_pzs": request_supply["list_pzs"],
        "num_ref_request": request_supply["num_ref_request"],
        "date_delivery": request_supply["date_request_delivery"]
    }


def requests_supply_schema(requests_supply) -> list:
    return [request_supply_schema(request_supply) for request_supply in requests_supply]
