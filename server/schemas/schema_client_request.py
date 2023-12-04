def requestClientEntity(data):
    return {
        "id": str(data["_id"]),
        "status": data["status"],
        "date_req": data["date_req"],
        "products": data["products"],
        "num_ref_solicitud": data["num_ref_solicitud"],
        "date_approved": data["date_approved"],
        "date_delivery_expected": data["date_delivery_expected"],
        "date_delivery": data["date_delivery"],
        "client": data["client"],
        "status": data["status"]

    }


def requestClientEntityInser(data):
    return {
        "status": data["status"],
        "date_req": data["date_req"],
        "products": data["products"],
        "num_ref_solicitud": data["num_ref_solicitud"],
        "date_approved": data["date_approved"],
        "date_delivery_expected": data["date_delivery_expected"],
        "date_delivery": data["date_delivery"],
        "client": data["client"],
        "status": data["status"]

    }


def requestsClientEntity(request) -> list:
    return [requestClientEntity(data) for data in request]
