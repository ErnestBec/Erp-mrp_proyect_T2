# Libreries
from starlette.status import HTTP_204_NO_CONTENT
from fastapi import HTTPException
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

# utils
from utils.db import db_name
# Schemas
from schemas.schema_orden_produccion import Ordenes_ProduccionEntity_month

# Controllers
from controllers.row_materials_controller import verified_mp
from controllers.notificationst_controller import create_notification


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
    create_notification(
        f"Se genero una nueva Orden de produccion", num_ref, num_ref)

    return fecha_prod_entrega

def get_order_production_month(month):

    data = db_name.OrderProduction.find()

    list_acount = []
    for request in list(data):
        fecha = request["fecha_alta"]
        mes = fecha.month
        if int(month) == int(mes):
            list_acount.append(request)

    return JSONResponse(content={"requests": Ordenes_ProduccionEntity_month(list_acount), "status": "Succes!"}, status_code=201)

