def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "Descripcion": item["Descripcion"],
        "min_stock": item["min_stock"],
        "max_stock": item["max_stock"],
        "precio_uni": item["precio_uni"],
        "num_pieza": item["num_pieza"],
        "cantidad": item["cantidad"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]