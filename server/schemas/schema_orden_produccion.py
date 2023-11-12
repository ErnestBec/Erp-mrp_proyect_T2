def orden_produccionEntity(data):
    return {
        "_id": str(data["_id"]),
        "fecha_alta": data["fecha_alta"],
        "solicitud": data["solicitud"],
        "producto": data["producto"],
        "cantidad_fabri": data["cantidad_fabri"],
        "id_pieza":data["id_pieza"]
    }


def Ordenes_ProduccionEntity(data) -> list:
    return [orden_produccionEntity(raw) for raw in data]
