from reactpy import component, html

@component
def btnFilter(opciones):
    dropdown_options = [
        html.li(html.a({"class": "dropdown-item", "href": "#"}, option)) for option in opciones
    ]

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
            html.b("Filtrar por"),
        ),
        html.ul({"class": "dropdown-menu"}, *dropdown_options),
    )
