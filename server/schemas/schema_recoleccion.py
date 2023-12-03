def recoleccionEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "fecha_recolection": item["fecha_recolection"],
        "fecha_entrega": item["fecha_entrega"],
        "cliente": item["cliente"],
        "status": item["status"],
        "num_ref_solicictud": item["num_ref_solicictud"],
        "costo": item["costo"]


    }


def recoleccionesEntity(entity) -> list:
    return [recoleccionEntity(item) for item in entity]
