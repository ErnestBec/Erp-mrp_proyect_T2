# Libreries
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
# utils
from utils.db import db_name
# Schemas
from schemas.request_suppply_schema import request_supply_schema, requests_supply_schema
from datetime import datetime
# utils
from utils.db import db_name


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
    id_pago = db_name.CuentasPagar.insert_one(
        {"proveedor": "Tier3", "importe": 4564, "fecha_pago": datetime.now(), "status": "pending"}).inserted_id
    # Se ingresa la peticion a tabla de peticiones a Proveedor
    date_deliverly = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")
    inserted = db_name.Request_Supplier.insert_one(
        {"fecha_peticion": datetime.now(), "fecha_entrega": date_deliverly, "id_pago": id_pago, "num_ref_request": num_ref, "status": "pending", "list_mp": mp}).inserted_id
    return date_deliverly


def create_request_supply(request_supplier):
    new_request_supplier = dict(request_supplier)
    new_request_supplier["date_delivery"] = datetime.now()
    id = db_name.RcepiptOfRequestSupplier.insert_one(
        new_request_supplier).inserted_id
    req_insert = db_name.RcepiptOfRequestSupplier.find_one({"_id": id})
    if not req_insert:
        raise HTTPException(
            detail="Error al insertar recibir la mp", status_code=400)
    # Cada que ingrese llegue embarque, verificamos si es de alguna produccion pendiente para completarla
    verifed_production_shipment(new_request_supplier["num_ref_request"])
    return JSONResponse(content={"Status": "Success!", "request": request_supply_schema(req_insert)})


def verifed_production_shipment(num_ref_request):
    order_production_pending = db_name.Request_Client.find_one(
        {"num_ref_solicitud": num_ref_request})

    if order_production_pending:
        # completamos Produccion y si sobra mp agregamos a almacen
        db_name.OrderProduction.update_one({"$and": [{"num_ref_solicitud": order_production_pending["num_ref_solicitud"]}]}, {
                                           "$set": {"status": "complete"}})
    # Si no hay pendientes agregamos a almacen
