
# utils
from utils.db import db_name
# Schemas
from datetime import datetime, timedelta
# utils
from utils.db import db_name
from controllers.notificationst_controller import create_notification


def request_proveedor(mp, num_ref):
    # Generamos los datos de la peticion que necesita proveedor
    # Cuerpo de Solicitud
    # {"num_ref_request": num_ref}
    # with httpx.Client() as client:
    #     headers = {"Authorization": 123123}
    #     response = client.post(os.getenv("URL_LOGISTICA"), headers=headers)
    # Proveedor me regresa costo de pedido, dia de entrega
    # Ingresamos a cuentas por pagar
    # verificamos que la mp este unificad
    date_pago = datetime.now()+timedelta(days=7)
    id_pago = db_name.CuentasPorPagar.insert_one(
        {"importe": 4564, "date_registration": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "date_pay": date_pago.strftime("%Y-%m-%d %H:%M:%S"), "Acreedor": "Tier3", "num_referencia": num_ref, "status": "pending"}).inserted_id
    create_notification(
        f"Se genero un nueva deuda", id_pago, num_ref)
    # Se ingresa la peticion a tabla de peticiones a Proveedor
    date_deliverly = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")
    inserted = db_name.Request_Supplier.insert_one(
        {"fecha_peticion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fecha_entrega": date_deliverly, "id_pago": id_pago, "num_ref_request": num_ref, "status": "pending", "list_mp": mp}).inserted_id
    create_notification(
        f"Se genero una nueva solicitud a proveedor", num_ref, num_ref)
    return date_deliverly
