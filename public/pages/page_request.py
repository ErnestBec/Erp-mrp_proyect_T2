from reactpy import component, html
from reactpy_router import link

@component
def page_request():
    return(
        html.div(
            html.h1("Hola Mundo!!!")
        )

    )