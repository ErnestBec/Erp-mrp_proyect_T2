# Libreries
from fastapi import FastAPI
from fastapi import HTTPException
from utils.appError_utils import http_error_handler, server_error_handler
from dotenv import load_dotenv
# Routes
from routes.routes_user import user
from routes.routes_products import product
from routes.routes_client_request import requests_client
from routes.routes_cuentas_por_cobrar import cuentacobrar
from routes.routes_raw_materials import raw_material
from routes.routes_cuentas_Pagar import cuentaPagar
from routes.routes_recoleccion import recoleccion
from routes.routes_OrderPrducc import OrdenProducc

from routes.routes_stock_materials import stock_materials


app = FastAPI()
# Manejo de Errores
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, server_error_handler)

# load env
load_dotenv()

# Routes
app.include_router(user)
app.include_router(product)
app.include_router(requests_client)
app.include_router(cuentacobrar)
app.include_router(raw_material)
app.include_router(cuentaPagar)
app.include_router(recoleccion)
app.include_router(OrdenProducc)

app.include_router(stock_materials)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
