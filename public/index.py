from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import home_page, login_page, shopping, error_page, card_page, Tables_pages, utilities_others, charts, register, utilities_animation, utilities_color, orders_page


@component
def App():
    return simple.router(
        route("/", home_page.home_page()),
        route("/login", login_page.login_user()),
        route("/register", register.register()),
        route("/shopping", shopping.shopping()),
        route("/cards", card_page.cards()),
        route("/tables", Tables_pages.tablas()),
        route("/utilothers", utilities_others.utlities_oters()),
        route("/utillitiesAnimation", utilities_animation.utilities_animation()),
        route("/utilitiesColor", utilities_color.utilities_color()),
        route("/charts", charts.graficas()),
        route("/orders", orders_page.order_page()),
        route("/perfil", charts.graficas()),
        route("*", error_page.error()),
    )


app = FastAPI()

configure(app, App)
