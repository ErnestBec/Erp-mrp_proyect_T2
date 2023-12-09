# libreries
import requests
import json
# utils
from utils.db import db_name
# Schemas
from datetime import datetime, timedelta
# utils
from utils.db import db_name
from controllers.notificationst_controller import create_notification


def request_proveedor(mp, num_ref):
    # Generamos los datos de la peticion que necesita proveedor
    list_mp_req=[]
    for req_mp in mp:
        list_mp_req.append({"id":req_mp["id_mp_prov"],"cantidad":str(req_mp["order_quantity"])})
    # Cuerpo de Solicitud
    date_deliverly = datetime.now()+timedelta(days=7)
    date_deliverly = date_deliverly.strftime("%Y-%m-%d %H:%M:%S")
    data_request =[{
    # "num_ref_solicitud":num_ref,
    "productos":list_mp_req,
    "fecha_pedido":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "fecha_entrega":date_deliverly, 
    "metodo_pago":"Tarjeta"
    }]
    try:
        requests.post("http://iproconnectmaterials.eastus.cloudapp.azure.com:8000/backend/postPedidoEntrante",data=json.dumps(data_request))
    except requests.exceptions.RequestException as e:
        print("Se creo notificacion de error")
        create_notification(
        f"Se genero un error al hacer la nueva solicitud a proveedor, verificarlo manualmente", num_ref, num_ref)

    date_pago = datetime.now()+timedelta(days=7)
    id_pago = db_name.CuentasPorPagar.insert_one(
        {"importe": 4564, "date_registration": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "date_pay": date_pago.strftime("%Y-%m-%d %H:%M:%S"), "Acreedor": "Tier3", "num_referencia": num_ref, "status": "pending"}).inserted_id
    create_notification(
        f"Se genero un nueva deuda", id_pago, num_ref)
    # Se ingresa la peticion a tabla de peticiones a Proveedor
    inserted = db_name.Request_Supplier.insert_one(
        {"fecha_peticion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fecha_entrega": date_deliverly, "id_pago": id_pago, "num_ref_request": num_ref, "status": "pending", "list_mp": mp}).inserted_id
    create_notification(
        f"Se genero una nueva solicitud a proveedor", num_ref, num_ref)
    return date_deliverly
