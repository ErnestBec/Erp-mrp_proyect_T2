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
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 30 días")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 3 meses")),
            html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 6 meses")),
            html.li(
                html.a({"class": "dropdown-item", "href": "#"}, "Últimos 12 meses")
            ),
        ),
    )
