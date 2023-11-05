def raw_materials(data):
    return {
        "_id": str(data["_id"]),
        "raw_material": data["raw_material"],
        "quantity": data["quantity"],
        "min_stock": data["min_stock"],
        "max_stock": data["max_stock"]
    }


def raws_materials(data) -> list:
    return [raw_materials(raw) for raw in data]
