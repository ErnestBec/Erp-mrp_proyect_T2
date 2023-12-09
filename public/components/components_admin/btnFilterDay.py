from reactpy import component, html


@component
def btnFilterDay():
    return html.div(
        {"class": "dropdown ms-2"},
        html.button(
            {
                "class": "btn btn-light dropdown-toggle",
                "type": "button",
                "style": "color: #000000;",
                "data-bs-toggle": "dropdown",
                "aria-expanded": "false",
            },
            html.i(
                {
                    "class": "bi bi-calendar",
                    "style": {
                        "fontSize": "16px",
                        "marginRight": "8px",
                        "fill": "currentColor",
                    },
                }
            ),
            html.b("Mostrar"),
        ),
        html.ul(
            {"class": "dropdown-menu"},
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Enero")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Febrero")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Marzo")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Abril")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Mayo")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Junio")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Julio")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Agosto")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Septiembre")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Octubre")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Noviembre")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Diciembre")),
        ),
    )
