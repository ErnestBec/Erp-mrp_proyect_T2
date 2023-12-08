from reactpy import component, use_reducer
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import EJEMPLOAPI, page_catalogo, page_store, page_forcast, page_racks, page_requests, page_orders, page_cuentas,page_login
# from reducers.reducer_login import session_reducer
# from reducers.store import SessionProvider
# from components import ProtectedRouter
# 
# 

@component
def App():
    # is_logged_in = use_selector(lambda state: state['is_logged_in'])

    return simple.router(
        # route("/", page_login.login_user()),
        route("/API", EJEMPLOAPI.App()),
        route("/Ordenes", page_orders.Page_Ordenes()),
        route("/Pronostico", page_forcast.Page_Forcast()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),
        route("/Almacenes", page_store.Page_Almacenes()),
        route("/Racks", page_racks.Page_Racks()),
        route("/Catalogo", page_catalogo.Page_Catalogo()),
        route("/login", page_login.login_user()),
        # route("/dashboard", ProtectedRouter.ProtectedRouter()),

    )

app = FastAPI()

configure(app, App)