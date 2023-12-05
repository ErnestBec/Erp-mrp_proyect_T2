from reactpy import component
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy_router import route, simple
from pages import login_page, error_page, page_request, dashboard,page_cuentas


@component
def App():
    return simple.router(
        route("/login", login_page.login_user()),
       
    

                
        route("/page_cuentas", page_cuentas.Page_Cuentas()),
        route("/page_dashboard", dashboard.Dashboard()),


        route("*", error_page.error()),
        route("/page_request", page_request.page_request()),

    )


app = FastAPI()

configure(app, App)
