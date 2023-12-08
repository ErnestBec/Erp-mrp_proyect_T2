def recoleccionEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "fecha_recolection": item["fecha_recolection"],
        "fecha_entrega": item["fecha_entrega"],
        "status": item["status"],
        "num_ref_solicictud": item["num_ref_solicictud"],
        "costo": item["costo"]
    }


def recoleccionesEntity(entity) -> list:
    return [recoleccionEntity(item) for item in entity]


def receivedEmbarkSchema(item) -> dict:
    return {
        "id": str(item["_id"]),
        "num_ref_solicitud": item["num_ref_solicitud"],
        "list_Mp": item["list_Mp"],
        "date_delivery": item["date_delivery"]
    }


def receivedEmbarksSchema(entity) -> list:
    return [receivedEmbarkSchema(item) for item in entity]
