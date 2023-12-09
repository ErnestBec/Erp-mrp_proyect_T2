from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages.pages_admin import page_catalogo_admin, page_store_admin, page_forcast_admin, page_racks_admin, page_requests_admin, page_orders_admin, page_cuentas_admin
from pages.pages_client import page_catalogo_user, page_requests_user, page_cuentas_user

@component
def App():
    return simple.router(
        #route("/API", EJEMPLOAPI.App()),
        route("/Admin_Ordenes", page_orders_admin.Page_Ordenes()),
        route("/Admin_Cuentas", page_cuentas_admin.Page_Cuentas()),
        route("/Admin_Pronostico", page_forcast_admin.Page_Forcast()),
        route("/Admin_Solicitudes", page_requests_admin.Page_Solicitudes()),
        route("/Admin_Almacenes", page_store_admin.Page_Almacenes()),
        route("/Admin_Racks", page_racks_admin.Page_Racks()),
        route("/Admin_Catalogo", page_catalogo_admin.Page_Catalogo()),

  
        route("/User_Solicitudes", page_requests_user.Page_Solicitudes()),
        route("/User_Cuentas", page_cuentas_user.Page_Cuentas()),
        route("/User_Catalogo", page_catalogo_user.Page_Catalogo()),
        
    )


app = FastAPI()

configure(app, App)
