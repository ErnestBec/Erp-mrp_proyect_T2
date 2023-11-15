def orden_produccionEntity(data):
    return {
        "_id": str(data["_id"]),
        "fecha_alta": data["fecha_alta"],
        "products": data["products"],
    }


def Ordenes_ProduccionEntity(data) -> list:
    return [orden_produccionEntity(raw) for raw in data]
