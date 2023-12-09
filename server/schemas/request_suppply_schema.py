def request_supply_schema(request_supply) -> dict:
    return {
        "_id": str(request_supply["_id"]),
        "list_mp": request_supply["list_mp"],
        "num_ref_request": request_supply["num_ref_request"],
        "fecha_peticion": request_supply["fecha_peticion"],
        "status":request_supply["status"]
    }


def requests_supply_schema(requests_supply) -> list:
    return [request_supply_schema(request_supply) for request_supply in requests_supply]
