def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name_prod": item["name_prod"],
        "Descripcion": item["Descripcion"],
        "min_stock": item["min_stock"],
        "max_stock": item["max_stock"],
        "precio_uni": item["precio_uni"],
        "num_pieza": item["num_pieza"],
        "mp": item["mp"],
        "time_production": item["time_production"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
