def cuenta_por_cobrarEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "solicitud": item["solicictud"],
        "importe": item["importe"],
        "fecha_emision": item["fecha_emision"],
        "total": item["total"],
        "fecha_de_pago": item["fcha_de_pago"]


    }


def cuentas_por_cobrarEntity(entity) -> list:
    return [cuenta_por_cobrarEntity(item) for item in entity]
