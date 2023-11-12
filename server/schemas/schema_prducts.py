def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name_prod": item["name_prod"],
        "Descripcion": item["Descripcion"],
        "min_stock": item["min_stock"],
        "max_stock": item["max_stock"],
        "precio_uni": item["precio_uni"],
        "num_pieza": item["num_pieza"],
        "category_prod": item["category_prod"],
        "cantidad_prod": item["catindad_prod"],
        "mp": item["mp"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
