from reactpy import component, html
from reactpy_router import link

@component
def NavbarBusqueda(titulo, icono):
    return html.div(
        html.nav(
            {
                "class": "navbar navbar-expand navbar-light bg-white topbar d-flex mb-3 static-top shadow container-fluid"
            },
            html.a(
                {
                    "href": "#",
                    "class": "btn",
                    "role": "button",
                    "type": "button",
                    "data-bs-toggle": "button",
                    "style": {"color": "black", "marginRight": "50%"},
                },
                html.i({"className": icono, "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(titulo),
            ),
            html.div(
                {
                    "class": "collapse navbar-collapse",
                    "id": "navbarSupportedContent",
                },
                html.ul(
                    {"class": "navbar-nav ml-auto"},
                    html.li(
                        {"class": "nav-item dropdown no-arrow"},
                        html.a(
                            {
                                "class": "nav-link dropdown-toggle",
                                "href": "#",
                                "id": "userDropdown",
                                "role": "button",
                                "data-toggle": "dropdown",
                                "aria-haspopup": "true",
                                "aria-expanded": "false",
                                "style": {"margin-left": "auto"},
                            },
                            html.i(
                                {
                                    "className": "bi bi-bell-fill",
                                    "style": {"fontSize": "22px", "color": "black", "margin-right": "0px"},
                                }
                            ),
                            html.i(
                                {
                                    "className": "bi bi-person-circle",
                                    "style": {"fontSize": "22px", "color": "black"},
                                }
                            ),
                        ),
                    ),
                ),
            ),
        )
    )