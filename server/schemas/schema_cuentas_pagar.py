def cuentaPagarEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "proveedopr": item["proveedor"],
        "solicitud": item["solicitud"],
        "importe": item["importe"],
        "total": item["total"],
        "fecha_de_pago": item["fecha_de_pago"]


    }


def cuentasPagarEntity(entity) -> list:
    return [cuentaPagarEntity(item) for item in entity]