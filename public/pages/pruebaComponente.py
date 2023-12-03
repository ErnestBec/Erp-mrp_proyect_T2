from reactpy import component, html
from components import navbar_top
from reactpy_router import link

@component
def Prueba():
    return html.div( {"style": {"display": "flex",},"id": "page-top"}, 
    
    navbar_top.NavbarBusqueda()

    )
