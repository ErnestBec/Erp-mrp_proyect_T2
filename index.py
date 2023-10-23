from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import home_page, login_page, shopping, error_page,card_page, Tables_pages, utilities_others


@component
def App():
    return simple.router(
        route("/", home_page.home_page()),
        route("/login", login_page.login_user()),
        route("/shopping", shopping.shopping()),
        route("/error", error_page.error()),
        route("/cards", card_page.cards()),
        route("/tables", Tables_pages.tablas()),
        route("/utilothers",utilities_others.utlities_oters())

    )


app = FastAPI()

configure(app, App)
