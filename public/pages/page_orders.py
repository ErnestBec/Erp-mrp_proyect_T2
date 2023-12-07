from reactpy import component, html, use_effect, use_state
from components import navbar_top, Card, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link
import requests
import json

def Estado(edo):
   
    if edo == "Aprobada":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#AFF2FF",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )
    if edo == "Pendiente":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#F0FE88",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )
    
    if edo == "Completada":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#5BDD4B",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )
    
    if edo == "No Empezada":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FF6060",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )


@component
def Page_Ordenes():
    orders, set_orders = use_state([])
    def getOrders():
            url ="http://127.0.0.1:8001/products"
            headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRpZXIyQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicHpzMTIzNDUiLCJleHAiOjE3MDIwNTMyNTZ9.B_Sx1RUI76Pn74oSUsDxYxBxUXsNpiLnOxLxdn-_K5I' }
            orders_api = requests.get(url,headers=headers)
            set_orders(orders_api)

    use_effect(getOrders, dependencies=[])

    titulo = "Ordenes"

    icono = 'bi bi-cart3'

    opciones = [
        "Total",
        "Pendiente",
        "Aprobada",
        "Completada",
    ]
    
    datos = [
        [
            "Aieto Energies",
            "Aprobada",
            "0957746KJLY",
            "BOM-Rizz-0523-001",
            "24/12/2020",
        ],
        [
            "Aieto Energies",
            "Pendiente",
            "0957746KJLY",
            "BOM-Rizz-0523-001",
            "24/12/2020",
        ],
        [
            "Aieto Energies",
            "Completada",
            "0957746KJLY",
            "BOM-Rizz-0523-001",
            "24/12/2020",
        ],
        [
            "Aieto Energies",
            "No Empezada",
            "0957746KJLY",
            "BOM-Rizz-0523-001",
            "24/12/2020",
        ],
    ]

    columnas = [
        "",
        "Nombre del Cliente",
        "Estado",
        "ID de la Orden",
        "Lista de Materiales",
        "Fecha de Vencimiento",
    ]

    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda(titulo, icono),
                    html.div(
                        {"class": "container-fluid"},
                        html.div(
                            {
                                "class": "card shadow mb-4",
                                "style": "background-color: white; border-radius:10px;",
                            },
                            html.div(
                                {
                                    "class": "container-fluid",
                                    "style": "margin-top: 5%; margin-bottom: 5%; color: #E8E8E8;",
                                },
                                html.div(
                                    {"class": "row"},
                                    html.div(
                                        {"class": "col-auto me-auto"},
                                        html.h6(
                                            {
                                                "class": "display-6",
                                                "style": "color: black;",
                                            },
                                    
                                            html.b(orders),
                                        ),
                                    ),
                                ),
                                html.div(
                                    {"class": "row"},
                                    html.div(
                                        {"class": "col-auto me-auto"},
                                        html.p(
                                            {
                                                "class": "display-8",
                                                "style": "color: black;",
                                            },
                                            "Estás viendo el número total de ordenes realizadas hasta el momento",
                                        ),
                                    ),
                                ),
                            ),
                            html.hr(
                                {
                                    "class": "sidebar-divider my-0",
                                    "style": "background-color: black; margin-top: 2%;",
                                }
                            ),
                            html.div(
                                {"class": "card-body", "style": "margin-top: 0%;"},
                                html.hr({"class": "sidebar-divider my-0"}),
                                html.div(
                                    {"class": "container-fluid"},
                                    html.div(
                                        {"class": "row no-border-bottom"},
                                        html.div(
                                            {"class": "col-auto"},
                                            html.div(
                                                {"class": "btn-group"},
                                                btnFilterDay.btnFilterDay(),
                                                btnFilter.btnFilter(opciones),
                                            ),
                                        ),
                                    ),
                                ),
                                tabla.Tabla(columnas, datos),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
