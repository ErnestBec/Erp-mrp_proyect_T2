def partnerEntity(data):
    return {
        "id": str(data["_id"]),
        "name": data["name"],
        "phone": data["phone"],
        "email": data["email"],
    }


def partnersEntity(partner) -> list:
    return [partnerEntity(data) for data in partner]
