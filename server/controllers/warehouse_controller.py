# Librerias
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
# Utils
from utils.db import db_name
# Schemas
from schemas.schemas_stock_materials import rack_stock, stock_product, type_stock, spaces_row
# Middlewares
from middlewares.warehouse_middleware import is_valid_object_id
# Controllers
from controllers.cuentaPagar_controller import create_cuentaPagar
from controllers.orden_produccion_controller import generate_Production
from controllers.notificationst_controller import create_notification
import httpx
import os
import time
from datetime import datetime


def create_warehouse_type(warehouse_type):
    new_warehouse_type = dict(warehouse_type)
    id = db_name.TypeWarehouse.insert_one(new_warehouse_type).inserted_id
    warehouse_type = db_name.TypeWarehouse.find_one({"_id": id})
    return JSONResponse(content={"warehouse_type": type_stock(warehouse_type), "status": "Success!"}, status_code=201)


def delete_warehouse_type(id):
    db_name.TypeWarehouse.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Warehouse


def create_warehouse(warehouse):
    new_warehouse = dict(warehouse)
    if not is_valid_object_id(new_warehouse["id_type_stock"]):
        raise HTTPException(
            status_code=400, detail="The id of type of warehouse invalid!")
    type_warehouse = db_name.TypeWarehouse.find_one(
        {"_id": ObjectId(new_warehouse["id_type_stock"])})
    if not type_warehouse:
        raise HTTPException(
            status_code=404, detail="The type warehouse doest not exist!")
    id = db_name.Warehouse.insert_one(new_warehouse).inserted_id
    new_warehouse = db_name.Warehouse.find_one({"_id": ObjectId(id)})
    new_warehouse["date_update"] = str(new_warehouse["date_update"])
    return JSONResponse(content={"warehouse_type": stock_product(new_warehouse), "status": "Success!"}, status_code=201)


def delete_warehouse(id):
    db_name.Warehouse.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Racks


def create_rack(rack):
    new_rack = dict(rack)
    if not is_valid_object_id(new_rack["id_stock"]):
        raise HTTPException(
            status_code=400, detail="The id of warehouse invalid!")
    warehouse = db_name.Warehouse.find_one(
        {"_id": ObjectId(new_rack["id_stock"])})
    if not warehouse:
        raise HTTPException(
            status_code=404, detail="The warehouse doest not exist!")
    id = db_name.Racks.insert_one(new_rack).inserted_id
    for i in range(0, new_rack["high_capacity"]):
        create_floor(
            {"id_rack": id, "long": new_rack["long_capacity"], "width_capacity": new_rack["width_capacity"]})
    new_rack = db_name.Racks.find_one({"_id": ObjectId(id)})
    new_rack["date_update"] = str(new_rack["date_update"])
    return JSONResponse(content={"warehouse_type": rack_stock(new_rack), "status": "Success!"}, status_code=201)


def delete_rack(id):
    db_name.Racks.delete_one({"_id": ObjectId(id)})
    return JSONResponse(content={"status": "Delete Successfull"}, status_code=204)

# Controllers Floors


def create_floor(floor):
    new_floor = dict(floor)
    id = db_name.Floors.insert_one(
        {"id_rack": new_floor["id_rack"]}).inserted_id
    for i in range(0, new_floor["long"]):
        create_row(
            {"id_floor": id, "width_capacity": new_floor["width_capacity"]})
    new_floor = db_name.Floors.find_one({"_id": ObjectId(id)})


def create_row(row):
    new_row = dict(row)
    id = db_name.Rows.insert_one({"id_floor": new_row["id_floor"]}).inserted_id
    for i in range(0, new_row["width_capacity"]):
        create_space_row({"id_row": id})
    new_row = db_name.Rows.find_one({"_id": ObjectId(id)})


def create_space_row(space_row_req):
    new_space_row = dict(space_row_req)
    id = db_name.SpaceRow.insert_one(
        {"id_row": new_space_row["id_row"], "id_prod_pz": "Null", "status": "free"}).inserted_id
    new_space_row = db_name.SpaceRow.find_one({"_id": ObjectId(id)})
    print(new_space_row)


def verified_almacen(products, num_ref, user):
    """
        Esta funcion verifica la existencia de productos terminados en almacen:
            -si no hay producto suficiente se genera una orden de produccion
            -Si si hay producto sificiente se genera una orden de recoleccion
        En cualquiera de los dos casos retorna un objeto con un valor boleano que indica si existen productos en almacen y la fecha de posible entrega al cliente dada por logistica:
            {"enough": True/False, "date": None/"01-20-2023", }

    """
    time_production = 0
    request_production = []
    list_products = []
    # Validamos almacen de productos terminados
    for product in products:
        product = dict(product)
        products_pzs = db_name.Products_Pza.count_documents(
            {"$and": [{"id_product": product["id_pro"]}, {"status": "active"}]})
        product_time = db_name.Products.find_one(
            {"_id": ObjectId(product["id_pro"])})
        list_products.append(product_time)
        time_production = time_production + \
            product_time["time_production"]
        # Verificamos que el producto se encuentre en existencia y ademas alcance
        if int(product["quantity"]) > products_pzs:
            # Se hace el conteo de la cantidad de productos faltantes para mandar a producción
            print("No alcanta el producto:")
            quantity_missing = product["quantity"]-products_pzs
            request_production.append(
                {"id_prod": product["id_pro"], "quantity_missing": quantity_missing})

    if len(request_production) == 0:
        # Se realiza la peticon a logistica para recoleccion, la fecha enviada sera la que logistica indique la entrega
        date_delivery = request_logistics(list_products, num_ref)
        # descontamos productos de Almacen
        discount_products(list_products)
        return date_delivery
    # Solicitamos la produccion
    date_production = generate_Production(
        request_production, num_ref, time_production)
    # Solcictamos Recoleccion
    date_delivery = request_logistics(list_products, num_ref, user)
    # Calculamos tiempo de entrega fecha de recoleccion mas tiempo de produccion
    # Convertir las cadenas a objetos datetime
    fecha_produccion = datetime.fromisoformat(
        date_production.replace("Z", "+00:00"))
    fecha_entrega = datetime.fromisoformat(
        date_delivery.replace("Z", "+00:00"))
    # Sumar las fechas
    fecha_sumada = fecha_produccion + (fecha_entrega - fecha_produccion)
    fecha_sumada_str = fecha_sumada.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_sumada_str


def discount_products(products):
    print(products)
    for product in products:
        if type(product) != dict:
            product = dict(product)
        products_pzs = db_name.Product_Pza.find(
            {"$and": [{"id_product": product["id_pro"]}, {"status": "active"}]})
        quantity = product["quantity"]
        products_pzs = list(products_pzs)
        for discount in range(len(products_pzs)):
            id_prod_pz = products_pzs[discount]
            db_name.Product_Pza.update_one(
                {"_id": id_prod_pz["_id"]}, {"$set": {"status": "sold"}})
            db_name.SpaceRow.update_one({"id_prod_pz": str(id_prod_pz["_id"])}, {
                                        "$set": {"status": "free", "id_prod_pz": "Null"}})


def request_logistics(list_products, num_ref_solicitud, user):

    # Generamos los datos de la peticion que necesita logistica
    # with httpx.Client() as client:
    #     headers = {"Authorization": 123123}
    #     response = client.post(os.getenv("URL_LOGISTICA"), headers=headers)
    # Logistica me regresa costo de recoleccion, dia de entrega a tier1, fecha de recoleccion t2
    # Si los productos de almacen Alcanzaron, se ingresa a cuentas por pagar
    print("solicita recoleccion ...")
    date_pago = datetime.now()+timedelta(days=7)
    id_prov = db_name.Recolections.insert_one(
        {"fecha_recolection": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fecha_entrega": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "num_ref_solicictud": num_ref_solicitud, "status": "pending", "costo": 159600}).inserted_id
    create_cuentaPagar({"importe": 15600, "date_registration": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                       "date_pay": date_pago.strftime("%Y-%m-%d %H:%M:%S"), "Acreedor": "Logistica", "num_referencia": id_prov, "status": "pending"})
    create_notification(
        f"Se genero una nueva solicitud a logistica", num_ref_solicitud, user["email"])
    # db_name.CuentasPagar.insert_one(
    #     {"proveedor": {"proveedor": "Logistica", "motivo": id_prov}, "importe": 4564, "fecha_pago": None, "status": "pending"})
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_all_space_rack_status(query_status, id_prod):
    if not is_valid_object_id(id_prod):
        raise HTTPException(
            status_code=400, detail="The id of tipe of rack invalid!")
    spaces = db_name.SpaceRow.find(
        {"$and": [{"status": query_status}, {"id_prod": id_prod}]})

    return {"status": spaces_row(spaces)}


# Se revisa si la orden de Materia prima recibida por logistica pertenece a una orden de produccion pendiente


def verify_request():
    return " "
