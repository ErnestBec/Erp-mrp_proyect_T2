from reactpy import component, html

@component
def BtnFilterDay():
    return (
        html.div(
        {"class_name": "dropdown ms-2"},
        html.button(
            {
                "class_name": "btn btn-light dropdown-toggle",
                "type": "button",
                "style": {"color": "#000000"},
                "data-bs-toggle": "dropdown",
                "aria-expanded": "false",
            },
            [
                html.i({"class_name": "bi bi-calendar-week"}),
                html.b("Mostrar"),
            ],
        ),
        html.ul(
            {"class_name": "dropdown-menu"},
            [
                html.li(html.a({"class_name": "dropdown-item", "href": "#"}, "Últimos 30 días")),
                html.li(html.a({"class_name": "dropdown-item", "href": "#"}, "Últimos 3 meses")),
                html.li(html.a({"class_name": "dropdown-item", "href": "#"}, "Últimos 6 meses")),
                html.li(html.a({"class_name": "dropdown-item", "href": "#"}, "Últimos 12 meses")),
            ],
        ),
    )


)

# Puedes usar BtnFilterDay() para renderizar este componente.
