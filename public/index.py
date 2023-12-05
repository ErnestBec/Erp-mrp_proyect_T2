from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple

from pages import EJEMPLOAPI, page_catalogo, page_store, page_forcast, page_racks, page_requests, page_orders, home_page, login_page, shopping, error_page, card_page, Tables_pages, utilities_others, charts, register, page_cuentas ,utilities_animation, utilities_color



@component
def App():
    return simple.router(
        route("/login", login_page.login_user()),
        route("/register", register.register()),
        route("/shopping", shopping.shopping()),
        route("/cards", card_page.cards()),
        route("/tables", Tables_pages.tablas()),
        route("/utilothers", utilities_others.utlities_oters()),
        route("/utillitiesAnimation", utilities_animation.utilities_animation()),
        route("/utilitiesColor", utilities_color.utilities_color()),
        route("/charts", charts.graficas()),
        route("/perfil", charts.graficas()),
        route("/API", EJEMPLOAPI.App()),
        route("/Ordenes", page_orders.Page_Ordenes()),
        route("/Pronostico", page_forcast.Page_Forcast()),
        route("/Solicitudes", page_requests.Page_Solicitudes()),
        route("/Almacenes", page_store.Page_Almacenes()),
        route("/Racks", page_racks.Page_Racks()),
        route("/Catalogo", page_catalogo.Page_Catalogo()),
        route("*", error_page.error()),
    )


app = FastAPI()

configure(app, App)
