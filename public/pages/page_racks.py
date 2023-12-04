from reactpy import component, html
from components import navbar_top, navbarMenu, tabla
from reactpy_router import link


def Capacidad(cap):
    if 0 < cap <= 9:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#F0FFA5",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )
    if 10 <= cap <= 29:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFD6A5",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )
    if 30 <= cap <= 49:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFBA67",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )
    if 50 <= cap <= 69:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFEA67",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )
    if 70 <= cap <= 89:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#CAF365",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )
    if 90 <= cap <= 100:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#50C242",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )

    if cap > 100:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FF0000",
                     "font-size": "14px"
                },
            },
             html.b(f"{cap}%"),
        )


@component
def Page_Racks():
    titulo = "Racks"

    icono = "bi bi-inboxes"

    datos = [
        ["mpelectronicos", "mp123435", Capacidad(80), "24/12/2020", "3", "4","3",],
        ["mpelectronicos", "mp123435", Capacidad(59), "24/12/2020", "3", "4","3",],
        ["mpelectronicos", "mp123435", Capacidad(30), "24/12/2020", "3", "4","3",],
        ["mpelectronicos", "mp123435", Capacidad(11), "24/12/2020", "3", "4","3",],
        
    ]

    columnas = [
        "",
        "Nombre",
        "Nombre Almacén",
        "Capacidad %",
        "Fecha de Actualización",
        "Pisos",
        "Filas",
        "Ancho de filas",
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
                                            html.b("Racks"),
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
                                            "Monitoreo de capacidad",
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
                                tabla.Tabla(columnas, datos),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
