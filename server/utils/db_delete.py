from pymongo import MongoClient


# Conectar a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Prueba_Tier2"]

# Collectiones DB
# Users
# coleccion = db["BusinessRuleMaxProd"]
# coleccion = db["CuentasPagar"]
# coleccion = db["CuentasPorCobrar"]
# coleccion = db["Floors"]
# coleccion = db["OrderProduction"]
# coleccion = db["Product_Pza"]
# coleccion = db["Products"]
# coleccion = db["Racks"]
# coleccion = db["RawMaterials"]
# coleccion = db["RcepiptOfRequestSupplier"]
# coleccion = db["Recolections"]
# coleccion = db["Request_Client"]
# coleccion = db["Request_Supplier"]
# coleccion = db["Rows"]
# coleccion = db["SpaceRow"]
# coleccion = db["TypeWarehouse"]
# coleccion = db["Warehouse"]
# coleccion = db["Notifications"]
coleccion = db[""]

# Borrar todos los documentos de la colección
coleccion.delete_many({})

print("Se han eliminado todos los documentos de la colección.")
