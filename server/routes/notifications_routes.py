from utils.db import db_name
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from bson import ObjectId
from datetime import datetime
# Middlewares
from middlewares.auth_middleware import Portador
# schemas
from schemas.notifications_schema import notifications_schema, notification_schema
notifications = APIRouter()


@notifications.get("/notifications-pending", tags=["Notifications"])
# En este caso en particular el middleware retoirna el valos del usuario logeado y estos datos se le envian al controlador como parametro 
def get_notifications_pending(user = Depends(Portador())):
    notifications_list = db_name.Notifications.find({"status": "pending","email_user": user["email"]})
    notifications_list = list(notifications_list)
    return JSONResponse(content={"notifications": notifications_schema(notifications_list)}, status_code=200)


@notifications.get("/notifications-views", tags=["Notifications"], dependencies=[Depends(Portador())])
def get_notifications_views():
    notifications_list = db_name.Notifications.find({"status": "view"})
    notifications_list = list(notifications_list)
    return JSONResponse(content={"notifications": notifications_schema(notifications_list)}, status_code=200)


@notifications.get("/notifications-user/{email}", tags=["Notifications"],dependencies=[Depends(Portador())])
def get_notifications_user(email):
    notifications_list = db_name.Notifications.find({"email_user": email})
    notifications_list = list(notifications_list)
    return JSONResponse(content={"notifications": notifications_schema(notifications_list)}, status_code=200)


@notifications.get("/all-notifications", tags=["Notifications"] ,dependencies=[Depends(Portador())])
def get_all_notifications():
    notifications_list = db_name.Notifications.find()
    notifications_list = list(notifications_list)
    return JSONResponse(content={"notifications": notifications_schema(notifications_list)}, status_code=200)


@notifications.put("/update-status/{id}", tags=["Notifications"],dependencies=[Depends(Portador())])
def notification_status(id: str):
    date_view = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_name.Notifications.update_one(
        {"_id": ObjectId(id)}, {"$set": {"status": "view", "date_view": date_view}})
    notification_update = db_name.Notifications.find_one({"_id": ObjectId(id)})
    notification_update = dict(notification_update)
    return JSONResponse(content={"notification": notification_schema(notification_update)}, status_code=201)
