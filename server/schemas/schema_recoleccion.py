def recoleccionEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "fecha": item["fecha"],
        "lugar": item["lugar"],
        "id_cobro": item["id_cobro"],
        "cobro": item["cobro"],
        "status":item["status"]


    }


def recoleccionesEntity(entity) -> list:
    return [recoleccionEntity(item) for item in entity]
