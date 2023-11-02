from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import home_page, login_page, shopping


@component
def App():
    return simple.router(
        route("/", home_page.home_page()),
        route("/login", login_page.login_user()),
        route("/shopping", shopping.shopping())
    )


app = FastAPI()

configure(app, App)
