def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "user": item["user"],
        "password": item["password"],
        "phone": item["phone"],
        "role": item["role"],
        "status": item["status"]
    }


def userEntityUpdate(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "user": item["user"],
        "phone": item["phone"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
