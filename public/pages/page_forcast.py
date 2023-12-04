from reactpy import component, html
from components import navbar_top, Card, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link


@component
def Page_Forcast():
    titulo = "Pronóstico"

    icono = "bi bi-graph-up"

    opciones = [
        "Ordenes Totales",
        "Ordenes Pendientes",
        "Ordenes Aprobadas",
        "Ordenes Completadas",
    ]

    datos = [
        [
            "1",
            "Aprobado",
            "BOM-Rizz-0523-001",
            "01/12/2020",
            "24/12/2020",
        ]
    ]

    columnas = [
        "",
        "ID Orden",
        "Estado",
        "Lista de Materiales",
        "Fecha de Inicio",
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
                                            html.b("Pronóstico"),
                                        ),
                                    ),
                                    html.div(
                                        {
                                            "class": "col-auto me-auto d-flex justify-content-between align-items-center"
                                        },
                                        html.button(
                                            {
                                                "type": "button",
                                                "class": "btn mb-2 mr-2",
                                                "style": {
                                                    "color": "#000000",
                                                    "background": "linear-gradient(0deg, #E8E8E8, #E8E8E8), linear-gradient(0deg, #111111, #111111)",
                                                },
                                            },
                                            html.b("Ver Historial"),
                                        ),
                                        html.button(
                                            {
                                                "type": "button",
                                                "class": "btn mb-2 ml-2",
                                                "style": {
                                                    "color": "#FFFFFF",
                                                    "background": "linear-gradient(0deg, #111111, #111111), linear-gradient(0deg, #E8E8E8, #E8E8E8)",
                                                },
                                            },
                                            html.b("Pronóstico >"),
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
