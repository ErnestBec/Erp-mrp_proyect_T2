# Libreries
from fastapi import Response
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from fastapi import HTTPException
import time
from datetime import datetime, timedelta
# utils
from utils.db import db_name
# Schemas
from schemas.schema_orden_produccion import orden_produccionEntity
# Controllers
from controllers.row_materials_controller import verified_mp


def generate_Production(request_production, num_ref, time_production):
    """
    Esta funcion genera la orden de produccion de los productos faltantes para completar la solicictud del cliente
        -Verifica almacen de materia prima
            -si alcanza hace el calculo del tiempo estimado de produccion y la retorna 
            -si no alcanza hace solicitud a t3 y retorna la fecha sumada de produccion mas fecha de entrega
    """
    # Verificamos la existencia de materia Prima
    info_mp = verified_mp(request_production, num_ref)
    # Si alcanza procedemos a Mandar a Produccion
    if info_mp["enough"]:
        date_now = datetime.now() + \
            timedelta(seconds=time_production)
        date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
        data_production = {"fecha_alta": datetime.now(),
                           "products": request_production, "fecha_termino": date_now, "num_ref_solicitud": num_ref, "status": "complete"}
        inserted = db_name.OrderProduction.insert_one(
            data_production).inserted_id
        if not inserted:
            raise HTTPException(
                status_code=500, detail="Error al mandar a producion los productos solicitado")
        return date_now

    date_now = datetime.now() + \
        timedelta(seconds=time_production)
    date_string = date_now.strftime("%Y-%m-%d %H:%M:%S")

    fecha_produccion = datetime.fromisoformat(
        date_string.replace("Z", "+00:00"))
    entrega_date_str = info_mp["date"]
    fecha_entrega = datetime.fromisoformat(
        entrega_date_str.replace("Z", "+00:00"))
    # Sumar las fechas
    fecha_sumada = fecha_produccion + (fecha_entrega - fecha_produccion)
    fecha_prod_entrega = fecha_sumada.strftime("%Y-%m-%d %H:%M:%S")
    data_production = {"fecha_alta": datetime.now(),
                       "products": request_production, "fecha_termino": fecha_sumada, "num_ref_solicitud": num_ref, "status": "pending"}
    inserted = db_name.OrderProduction.insert_one(
        data_production).inserted_id

    return fecha_prod_entrega


def create_orden_produccion(orden):
    new_orden = dict(orden)
    id = db_name.OrdenesProduccion.insert_one(new_orden).inserted_id
    ord = db_name.OrdenesProduccion.find_one({"_id": id})
    return orden_produccionEntity(ord)


def get_Orden_produccion(id):
    orden = db_name.OrdenesProduccion.find_one({"_id": ObjectId(id)})
    return orden_produccionEntity(orden)


def update_Orden_prooduccion(id, orden):
    db_name.OrdenesProduccion.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(orden)})
    return orden_produccionEntity(db_name.OrdenesProduccion.find_one({"_id": ObjectId(id)}))


def delete_Orden_Produccion(id):
    db_name.OrdenesProduccion.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
