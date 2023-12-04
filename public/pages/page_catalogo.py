from reactpy import component, html
from components import navbar_top, Card, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link

def Boom():

     return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#D2DDE7",
                },
            },
             html.b(html.a({"href": "#", "style": {"color": "black", "font-size": "14px"}}, "Ver BOOM"))

        ) 

def Estado(edo):
    if edo == "Disponible":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#DFFFEE",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )
    if edo == "No Disponible":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFDFDF",
                     "font-size": "14px"
                },
            },
             html.b(f"{edo}"),
        )
    

@component
def Page_Catalogo():

    titulo = "Catálogo"

    icono = 'bi bi-bag'

    opciones = [
        "Disponible",
        "No Disponible",
    ]

    datos = [["65545", "Pantallas", Estado("Disponible"), "11", "99", "$123", Boom()],
             ["65545", "Pantallas", Estado("No Disponible"), "11", "99", "$123", Boom()],]

    columnas = [
        "",
        "ID",
        "Nombre del Producto",
        "Estado",
        "Stock Mínimo",
        "Stock Máximo",
        "Precio",
        "",
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
                                            html.b("Catálogo"),
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
                                            "Disponibilidad",
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
