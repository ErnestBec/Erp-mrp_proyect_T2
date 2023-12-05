from reactpy import component, html
from components import navbar_top, Card, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link

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
    
def Ver():
     return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#D2DDE7",
                },
            },
             html.b(html.a({"href": "#", "style": {"color": "black", "font-size": "14px"}}, "Ver"))

        ) 

@component
def Page_Solicitudes():

    titulo = "Solicitudes"

    icono = 'bi bi-card-list'

    opciones = [
        "Solicitudes Aprobadas",
        "Solicitudes Pendientes",
    ]

   

    datos = [
    [
        "Aieto Energies",
        "0957746KJLY",
        Ver(),  
        Estado("Aprobada"),
        "01/12/2020",
        "24/12/2020",
    ],
    [
        "Aieto Energies",
        "0957746KJLY",
        Ver(),  
        Estado("Pendiente"),
        "01/12/2020",
        "24/12/2020",
    ],
    ]
    columnas = [
        "",
        "Nombre del Cliente",
        "Num. referencia",
        "Descripción",
        "Estado",
        "Fecha de emisión",
        "Fecha de entrega",
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
                                            html.b("Inventario de Solicitudes"),
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
                                            "Listado de todas las solicitudes esperando aprobación",
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
