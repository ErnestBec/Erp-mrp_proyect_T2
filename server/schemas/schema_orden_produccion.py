def orden_produccionEntity(data):
    return {
        "_id": str(data["_id"]),
        "fecha_alta": data["fecha_alta"],
        "products": data["products"],
        "fecha_termino":data["fecha_termino"],
        "num_ref_solicitud":data["num_ref_solicitud"],
        "status":data["status"]
    }


def Ordenes_ProduccionEntity(data) -> list:
    return [orden_produccionEntity(raw) for raw in data]

def orden_produccionEntity_month(data):
    return {
        "_id": str(data["_id"]),
        "fecha_alta": str(data["fecha_alta"]),
        "products": data["products"],
        "fecha_termino":str(data["fecha_termino"]),
        "num_ref_solicitud":data["num_ref_solicitud"],
        "status":data["status"]
    }


def Ordenes_ProduccionEntity_month(data) -> list:
    return [orden_produccionEntity_month(raw) for raw in data]
