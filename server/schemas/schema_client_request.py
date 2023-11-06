def requestClientEntity(data):
    return {
        "id": str(data["_id"]),
        "status": data["status"],
        "client": data["client"],
        "date_req": data["date_req"],
        "products": data["products"],
        "num_ref_solicitud": data["num_ref_solicitud"],
        "date_approved": data["date_approved"],
        "date_delivery_expected": data["date_delivery_expected"],
        "date_delivery": data["date_delivery"]

    }


def requestClientEntityInser(data):
    return {
        "status": data["status"],
        "client": data["client"],
        "date_req": data["date_req"],
        "products": data["products"],
        "num_ref_solicitud": data["num_ref_solicitud"],
        "date_approved": data["date_approved"],
        "date_delivery_expected": data["date_delivery_expected"],
        "date_delivery": data["date_delivery"]

    }


def requestsClientEntity(request) -> list:
    return [requestClientEntity(data) for data in request]
 
 