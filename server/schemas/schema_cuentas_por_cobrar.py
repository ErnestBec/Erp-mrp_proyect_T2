def cuenta_por_cobrarEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "importe": item["importe"],
        "date_registration": item["date_registration"],
        "date_pay": item["date_pay"],
        "Deudor": item["Deudor"],
        "num_referencia": item["num_referencia"],
        "status": item["status"]
    }


def cuentas_por_cobrarEntity(entity) -> list:
    return [cuenta_por_cobrarEntity(item) for item in entity]
