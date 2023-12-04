from reactpy import component, html
from components import navbar_top, Card, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link


@component
def Page_Ordenes():

    titulo = "Ordenes"

    icono = 'bi bi-cart3'

    opciones = [
        "Ordenes Totales",
        "Ordenes Pendientes",
        "Ordenes Aprobadas",
        "Ordenes Completadas",
    ]

    datos = [
        [
            "Aieto Energies",
            "Aprobado",
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
                                            html.b("Ordenes Totales"),
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
