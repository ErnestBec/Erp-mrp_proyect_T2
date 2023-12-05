from reactpy import component, html
from reactpy_router import link


@component
def NavbarBusqueda(titulo, icono):

    return html.div(
        html.nav(
            {
                "class": "navbar navbar-expand navbar-light bg-white topbar d-flex mb-3 static-top shadow"
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

                #html.i({"className": "bi bi-cash d-flex", "style": {"fontSize": "20px"}}),

                html.i({"className": icono, "style": {"fontSize": "20px"}}),

                html.b(titulo),
            ),
            html.input(
                {
                    "type": "email",
                    "class": "form-control navbar-nav ml-auto",
                    "id": "floatingInput",
                    "placeholder": "Buscar ...",
                    "aria-label": "Search",
                }
            ),
            html.a(
                {
                    "class": "nav-link dropdown-toggle",
                    "href": "#",
                    "id": "userDropdown",
                    "role": "button",
                    "data-toggle": "dropdown",
                    "aria-haspopup": "true",
                    "aria-expanded": "false",
                },
                html.i(
                    {
                        "className": "bi bi-bell-fill",
                        "style": {"fontSize": "22px", "color": "black", "margin-right":"10px"},
                    }
                ),
                html.i(
                    {
                        "className": "bi bi-person-circle",
                        "style": {"fontSize": "22px", "color": "black"},
                    }
                ),
            ),
        )
    )






