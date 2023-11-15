def product_pieza_schema(product_pieza) -> dict:
    return {
        "_id": str(product_pieza["_id"]),
        "id_product": product_pieza["id_product"],
        "status": product_pieza["status"],
        "date": product_pieza["date"]
    }


def products_pieza_schema(products_pza) -> list:
    return [product_pieza_schema(product) for product in products_pza]
