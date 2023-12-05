from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple

from pages import EJEMPLOAPI, page_catalogo, page_store, page_forcast, page_racks, page_requests, page_orders,login_page,  error_page,  page_cuentas, dashboard



@component
def App():
    return simple.router(
        route("/login", login_page.login_user()),
        route("/page_cuentas", page_cuentas.Page_Cuentas()),
        route("/API", EJEMPLOAPI.App()),
        route("/Ordenes", page_orders.Page_Ordenes()),
        route("/Pronostico", page_forcast.Page_Forcast()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),
        route("/Almacenes", page_store.Page_Almacenes()),
        route("/Racks", page_racks.Page_Racks()),
        route("/Catalogo", page_catalogo.Page_Catalogo()),
        route("/page_dashboard", dashboard.Dashboard()),

        route("*", error_page.error()),
    )


app = FastAPI()

configure(app, App)
