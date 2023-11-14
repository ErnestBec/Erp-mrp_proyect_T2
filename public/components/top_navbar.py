from reactpy import component, html
from reactpy_router import link


@component
def navbar_top():
    return (
        html.nav({"class": "navbar border-bottom border-body"},
                 html.h1("Huevos"))
    )
