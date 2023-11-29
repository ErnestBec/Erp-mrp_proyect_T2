def stock_rackspace_Entity(data) -> dict:
    return {
        "_id": str(data["_id"]),
        "name": data["name"],
        "product_stored": data["product_stored"]
    }


def stocks_spacesRacks_Entity(data) -> list:
    return [stock_rackspace_Entity(item) for item in data]


def stock_rack_Entity(data) -> dict:
    return {
        "_id": str(data["_id"]),
        "name": data["name"],
        "spaces": data["spaces"],
    }


def stocks_racks_Entity(data) -> list:
    return [stock_rack_Entity(item) for item in data]


def stock_row_Entity(data) -> dict:
    return {
        "_id": str(data["_id"]),
        "name": data["name"],
        "racks": data["racks"],
    }


def stock_floor_Entity(data) -> dict:
    return {
        "_id": str(data["_id"]),
        "name": data["name"],
        "rows": data["rows"],
    }
