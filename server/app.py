# Es el archivo principal de la api, aqui se crea una nueva instancia de FastApi ademas de que se hace el ruteo principal de cada Modelo de la base de datos y sus controladores
# Libreries
from fastapi import FastAPI
from fastapi import HTTPException
from utils.appError_utils import http_error_handler, server_error_handler
from dotenv import load_dotenv
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# Routes
from routes.routes_user import user
from routes.routes_products import product
from routes.routes_client_request import requests_client
from routes.routes_cuentas_por_cobrar import cuentacobrar
from routes.routes_raw_materials import raw_material
from routes.routes_cuentas_Pagar import cuentaPagar
from routes.routes_recoleccion import recoleccion
from routes.routes_OrderPrducc import OrdenProducc
from routes.Business_Rules_routes import routes_business_rules
from routes.routes_stock_materials import stock_materials
from routes.notifications_routes import notifications
from routes.routes_request_Supply import request_Supply

# Se genera una nueva instancia para la API desde FastApi para levantar nuesta aplicacion
app = FastAPI()
# Indicamos a nuestra aplicacion que utilice las funciones especificadas, son quienes capturan los errores de servidor ademas de errores personalizados
# Manejo de Errores
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, server_error_handler)

# Indicamos que todo nuestro proyecto este a la escucha de las valiabres de entorno declaradas en el archivo .env
# load env
load_dotenv()

# Agragamos el middlegare que permite utilizar cors dentro de cada peticion, es decir que permita al acceso a todo tipo de peticiones desde cuanquier direccion
# Permitir las cors
app.add_middleware(
    CORSMiddleware,
    # Puedes especificar los orígenes permitidos en lugar de "*"
    allow_origins=["*"],
    allow_credentials=True,
    # Puedes especificar los métodos permitidos (por ejemplo, ["GET", "POST"])
    allow_methods=["*"],
    # Puedes especificar los encabezados permitidos (por ejemplo, ["Content-Type"])
    allow_headers=["*"],
)

# Indicamos a  nuestra aplicacion cuales son las rutas que tendra registradas, esto proviene de la carpeta routes que son rutas personalizadas para cada modelo y contrlador
# Routes
app.include_router(user)
app.include_router(product)
app.include_router(requests_client)
app.include_router(request_Supply)
app.include_router(cuentacobrar)
app.include_router(cuentaPagar)
app.include_router(stock_materials)
app.include_router(raw_material)
app.include_router(recoleccion)
app.include_router(OrdenProducc)
app.include_router(routes_business_rules)
app.include_router(notifications)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRpZXIyQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicHpzMTIzNDUiLCJleHAiOjE3MDIxMjU1NTh9.zW4JbVwrPleTeeSLNZLmVwjaclBfsDOebDsJ97P66tw
# Inicializa el proyecto en el local host aqui indicamos en que puerto se inicializara, esto solo es cuando no se ejecuta el proyecto con el comando uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
