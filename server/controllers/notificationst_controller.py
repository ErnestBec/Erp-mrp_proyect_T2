from datetime import datetime
from utils.db import db_name


def create_notification(message, id_message, email_user):
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_name.Notifications.insert_one({"Mesaage": message, "id_message": id_message,
                                     "date_created": date_created, "date_view": None, "email_user": email_user, "status": "pending"})
