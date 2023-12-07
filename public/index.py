from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import page_catalogo, page_store, page_forcast, page_racks, page_requests, page_orders, page_cuentas

@component
def App():
    return simple.router(
        #route("/API", EJEMPLOAPI.App()),
        route("/Ordenes", page_orders.Page_Ordenes()),
        route("/Pronostico", page_forcast.Page_Forcast()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),
        route("/Almacenes", page_store.Page_Almacenes()),
        route("/Racks", page_racks.Page_Racks()),
        route("/Catalogo", page_catalogo.Page_Catalogo()),
        
    )


app = FastAPI()

configure(app, App)
