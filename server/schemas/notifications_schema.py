def notification_schema(notification) -> dict:
    return {
        "_id": str(notification["_id"]),
        "Mesaage": notification["Mesaage"],
        "id_message": str(notification["id_message"]),
        "date_created": notification["date_created"],
        "date_view": notification["date_view"],
        "email_user": str(notification["email_user"]),
        "status": notification["status"]
    }


def notifications_schema(notifications) -> list:
    return [notification_schema(notification) for notification in notifications]
