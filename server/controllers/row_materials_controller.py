from utils.db import db_name
from fastapi import Response
from schemas.raw_materials import raw_materials
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from controllers.request_supply_controller import request_proveedor
from datetime import datetime, timedelta


def create_rawMaterial(raw):
    new_rawmat = dict(raw)
    id = db_name.RawMaterials.insert_one(new_rawmat).inserted_id
    cuenta = db_name.RawMaterials.find_one({"_id": id})
    return raw_materials(cuenta)


def get_rawMaterial(id):
    rawmat = db_name.RawMaterials.find_one({"_id": ObjectId(id)})
    return raw_materials(rawmat)


def update_rawMaterial(id, raw):
    db_name.RawMaterials.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(raw)})
    return raw_materials(db_name.RawMaterials.find_one({"_id": ObjectId(id)}))


def delete_rawMaterial(id):
    db_name.RawMaterials.find_one_and_delete(
        {"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)


def verified_mp(products, num_ref):
    request_mp = []
    discount_mp = []
    for product in products:
        product_mp = db_name.Products.find_one(
            {"_id": ObjectId(product["id_prod"])})
        for mp in product_mp["mp"]:
            wareHouse_mp = db_name.Product_Pza.count_documents(
                {"$and": [{"id_product": mp["id_mp"]}, {"status": "active"}]})
            if mp["quantyti"] > wareHouse_mp:
                print("añadiendo mp a pedir")
                request_mp.append({"id_mp": mp["id_mp"], "order_quantity": int(
                    mp["quantyti"])-int(wareHouse_mp)})
            # Listamos Mp para descontar de almacen
            discount_mp.append({"id_mp": mp["id_mp"], "order_quantity": int(
                mp["quantyti"])})
    print(len(request_mp))
    if len(request_mp) == 0:
        # Descontamos de Mp de Almacenes
        discount_Mp(discount_mp)
        return {"enough": True, "date": datetime.now()}
    # Si no lacanza Hacemos peticion a T3 para solicictar MP y creamos Orden de produccion en estado pendiente
    date_deliverly = request_proveedor(request_mp, num_ref)
    return {"enough": False, "date": date_deliverly}


# Descuenta productos de Almacen de Materia Prima


def discount_Mp(list_mp):
    for mp in list_mp:
        print(mp)
        mp_pzs = db_name.Product_Pza.find(
            {"$and": [{"id_product": mp["id_mp"]}, {"status": "active"}]})
        quantity = mp["order_quantity"]
        mp_pzs = list(mp_pzs)
        print(len(mp_pzs))

        for discount in range(len(mp_pzs)):
            id_mp_pz = mp_pzs[discount]
            print(id_mp_pz)
            db_name.Product_Pza.update_one(
                {"_id": id_mp_pz["_id"]}, {"$set": {"status": "sold"}})
            db_name.SpaceRow.update_one({"id_prod_pz": id_mp_pz["_id"]}, {
                "$set": {"status": "free", "id_prod_pz": "Null"}})
