def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "emal": item["email"],
        "user": item["user"],
        "password": item["password"],
        "phone": item["phone"],
        "role": item["role"],
        "status": item["status"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
