from pymongo import MongoClient
import os

db_hostname = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
conn = MongoClient(db_hostname, db_port)

db_name = conn.Prueba_Tier2
