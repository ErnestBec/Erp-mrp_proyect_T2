def cuentaPagarEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "importe": item["importe"],
        "date_registration": item["date_registration"],
        "date_pay": item["date_pay"],
        "Acreedor": item["Acreedor"],
        "num_referencia": str(item["num_referencia"]),
        "status": item["status"],



    }


def cuentasPagarEntity(entity) -> list:
    return [cuentaPagarEntity(item) for item in entity]
