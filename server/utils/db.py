from pymongo import MongoClient
import os
# Solo genera la conexion a la base de datos e indicamos el nombre de la bd para solo pasrla a las demas funciones y no estar abriendo la conexion muchas veces
db_hostname = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
conn = MongoClient(db_hostname, db_port)

db_name = conn.Prueba_Tier2
