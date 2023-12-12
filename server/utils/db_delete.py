from pymongo import MongoClient

# Esta solo es para borrar el contenido de las colecciones, no influye en la API jajajaaj xd
# Conectar a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Prueba_Tier2"]

# Collectiones DB
# #coleccion = db["RcepiptOfRequestSupplier"]
# coleccion = db["Notifications"]
# Users
# coleccion = db["BusinessRuleMaxProd"]
# coleccion = db["CuentasPagar"]
# collections = ["CuentasPorCobrar","Floors","OrderProduction","Product_Pza","Products","Racks",]
# coleccion = db["CuentasPorCobrar"]
# coleccion = db["Floors"]
# coleccion = db["OrderProduction"]
# coleccion = db["Product_Pza"]
# coleccion = db["Products"]
# coleccion = db["Racks"]
# coleccion = db["RawMaterials"]
# coleccion = db["Recolections"]
# coleccion = db["Request_Client"]
# coleccion = db["Request_Supplier"]
# coleccion = db["Rows"]
# coleccion = db["SpaceRow"]
# coleccion = db["TypeWarehouse"]
# coleccion = db["Warehouse"]
# coleccion = db[""]

# Borrar todos los documentos de la colección
coleccion.delete_many({})

print("Se han eliminado todos los documentos de la colección.")
