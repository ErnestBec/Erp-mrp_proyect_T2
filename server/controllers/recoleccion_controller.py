# Libreries
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from utils.db import db_name
import random
from fastapi import Response
from schemas.schema_recoleccion import recoleccionEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from schemas.request_suppply_schema import request_supply_schema, requests_supply_schema
from schemas.schema_recoleccion import receivedEmbarkSchema
from controllers.row_materials_controller import discount_Mp
from controllers.warehouse_controller import discount_products
from controllers.notificationst_controller import create_notification


def embark_logistics():
    ""


def receive_request_Logistics(request_supplier):
    new_request_supplier = dict(request_supplier)
    new_request_supplier["date_delivery"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")
    for mp in new_request_supplier["list_Mp"]:
        mp = dict(mp)
    id = db_name.RcepiptOfRequestSupplier.insert_one(
        new_request_supplier).inserted_id
    req_insert = db_name.RcepiptOfRequestSupplier.find_one({"_id": id})
    create_notification(
        f"Se recibio materia prima de logisitca", id, id)
    if not req_insert:
        raise HTTPException(
            detail="Error al insertar recibir la mp", status_code=400)
    # actualizamos estado de solicitud de cliente
    # Cada que ingrese llegue embarque, verificamos si es de alguna produccion pendiente para completarla
    verifed_production_shipment(
        new_request_supplier["num_ref_solicitud"], new_request_supplier["list_Mp"])
    return JSONResponse(content={"Status": "Success!", "request": receivedEmbarkSchema(req_insert)})


def verifed_production_shipment(num_ref_request, list_mp):
    # verificamos si sobra mp de la prodcution
    for mp in list_mp:
        db_name.Product_Pza.insert_one({"no_serie": generar_numero_serie(),
                                        "id_product": mp["id_mp"],
                                        "status": "active",
                                        "date": {
            "$date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }}).inserted_id
        list_spaces = db_name.SpaceRow.find({"status": "free"})
        list_spaces = list(list_spaces)
        if len(list_spaces) < 10:
            raise HTTPException(
                detail="Ya no hay espacio en almacen", status_code=404)
        space_insert = list_spaces[0]
        db_name.SpaceRow.update_one({"_id": space_insert["_id"]}, {
                                    "$set": {"id_prod_pz": mp["id_mp"], "status": "ocuped"}})

    # Descontamos Mp utilixada en produccion
    discount_Mp(list_mp)
    db_name.OrderProduction.update_one({"$and": [{"num_ref_solicitud": num_ref_request}]}, {
        "$set": {"status": "complete"}})
    create_notification(
        f"Se termino la opdern de produccion {num_ref_request}", num_ref_request, num_ref_request)
    Order_production = db_name.OrderProduction.find_one(
        {"num_ref_solicitud": num_ref_request})
    list_products = [
        {'id_pro': '6554505975595ec9eb847586', 'quantity': 5}, {'id_pro': '6554505975595ec9eb847586', 'quantity': 5}]
    discount_products(list_products)
    print("los productos fueron descontados")
    db_name.Request_Supplier.update_one(
        {"num_ref_request": num_ref_request}, {"$set": {"status": "complete"}})
    print("se actualizo el estado de proveedor")
    db_name.Request_Client.update_one(
        {"num_ref_solicitud": num_ref_request}, {"$set": {"status": "complete"}})
    create_notification(
        f"Se completo la solicitud de cliente con referencia {num_ref_request}", num_ref_request, num_ref_request)
    print("se actualizo el estado de request cliente")


def cambiar_nombre_propiedad(objeto):
    if 'id_product' in objeto:
        objeto['id_pro'] = objeto.pop('id_product')
    return objeto


def generar_numero_serie():
    # Genera un número de serie de 10 dígitos
    numero_serie = ''.join(random.choice('0123456789') for _ in range(10))
    return numero_serie


def create_Recoleccion(recoleccion):
    new_recoleccion = dict(recoleccion)
    id = db_name.Recolecciones.insert_one(new_recoleccion).inserted_id
    recol = db_name.Recolecciones.find_one({"_id": id})
    return recoleccionEntity(recol)


def get_Recolecciom(id):
    product = db_name.Recolecciones.find_one({"_id": ObjectId(id)})
    return recoleccionEntity(product)


def update_recoleccion(id, recoleccion):
    db_name.Recolecciones.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(recoleccion)})
    return recoleccionEntity(db_name.Recolecciones.find_one({"_id": ObjectId(id)}))


def delete_recoleccion(id):
    db_name.Recolecciones.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
