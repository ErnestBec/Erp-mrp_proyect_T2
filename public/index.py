from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
<<<<<<< HEAD
from pages import EJEMPLOAPI, page_catalogo, page_store, page_forcast, page_racks, page_requests, page_orders, page_cuentas

=======
from pages.pages_admin import page_catalogo_admin, page_store_admin, page_forcast_admin, page_racks_admin, page_requests_admin, page_orders_admin, page_cuentas_admin
from pages.pages_client import page_catalogo_user, page_requests_user, page_cuentas_user
>>>>>>> 3306572dd66718324ab3b1fe1ba08850a2c7d3ff

@component
def App():
    return simple.router(
<<<<<<< HEAD
        route("/API", EJEMPLOAPI.App()),
        route("/Ordenes", page_orders.Page_Ordenes()),
        route("/Pronostico", page_forcast.Page_Forcast()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),
        route("/Almacenes", page_store.Page_Almacenes()),
        route("/Racks", page_racks.Page_Racks()),
        route("/Catalogo", page_catalogo.Page_Catalogo()),

=======
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
        
>>>>>>> 3306572dd66718324ab3b1fe1ba08850a2c7d3ff
    )


app = FastAPI()

configure(app, App)
