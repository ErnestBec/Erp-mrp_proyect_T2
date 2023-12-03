from reactpy import component, html

@component
def Card():
    return (
        html.div(
            {"class": "card shadow mb-4", "style": {"backgroundColor": "white", "borderRadius": "10px"}},
            html.div(
                {"class": "container-fluid", "style": {"marginTop": "5%", "marginBottom": "5%", "color": "#E8E8E8"}},
                html.div(
                    {"class": "row d-flex align-items-center"},
                    html.div(
                        {"class": "col-auto me-auto"},
                        html.h6(
                            {"class": "display-6", "style": {"color": "black"}},
                            html.b("Pronóstico")
                        )
                    ),
                    html.div(
                        {"class": "col-auto me-auto d-flex justify-content-between align-items-center"},
                        html.button(
                            {"type": "button", "class": "btn mb-2 mr-2", "style": {"color": "#000000", "background": "linear-gradient(0deg, #E8E8E8, #E8E8E8), linear-gradient(0deg, #111111, #111111)"}},
                            html.b("Ver Historial")
                        ),
                        html.button(
                            {"type": "button", "class": "btn mb-2 ml-2", "style": {"color": "#FFFFFF", "background": "linear-gradient(0deg, #111111, #111111), linear-gradient(0deg, #E8E8E8, #E8E8E8)"}},
                            html.b("Pronóstico >")
                        )
                    )
                )
            ),
            html.hr({"class": "sidebar-divider my-0", "style": {"backgroundColor": "black", "marginTop": "5%"}}),
            html.div(
                {"class": "card-body", "style": {"marginTop": "0%"}},
                html.hr({"class": "sidebar-divider my-0"}),
                html.div(
                    {"class": "container-fluid"},
                    html.div(
                        {"class": "row no-border-bottom"},
                        html.div(
                            {"class": "col-auto"},
                            html.div(
                                {"class": "btn-group"},
                                html.div(
                                    {"class": "dropdown ms-2"},
                                    html.button(
                                        {"class": "btn btn-light dropdown-toggle", "type": "button", "style": {"color": "#000000"}, "data-bs-toggle": "dropdown", "aria-expanded": "false"},
                                        html.svg(
                                            {"xmlns": "http://www.w3.org/2000/svg", "width": "16", "height": "16", "fill": "currentColor", "class": "bi bi-calendar", "viewBox": "0 0 16 16", "style": {"marginRight": "8px"}},
                                            html.path({"d": "M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4z"})
                                        ),
                                        html.b("Mostrar")
                                    ),
                                    html.ul(
                                        {"class": "dropdown-menu"},
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 30 días")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 3 meses")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 6 meses")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Últimos 12 meses"))
                                    )
                                ),
                                html.div(
                                    {"class": "dropdown ms-2"},
                                    html.button(
                                        {"class": "btn btn-light dropdown-toggle", "type": "button", "style": {"color": "#000000"}, "data-bs-toggle": "dropdown", "aria-expanded": "false"},
                                        html.b("Filtrar por")
                                    ),
                                    html.ul(
                                        {"class": "dropdown-menu"},
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Ordenes Totales")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Ordenes Pendientes")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Ordenes Aprobadas")),
                                        html.li(html.a({"class": "dropdown-item", "href": "#"}, "Ordenes Completadas"))
                                    )
                                )
                            )
                        )
                    )
                ),
                html.div(
                    {"class": "table-responsive", "style": {"marginTop": "2%"}},
                    html.table(
                        {"class": "table", "id": "dataTable"},
                        html.thead(
                            {"style": {"textAlign": "center"}},
                            html.tr(
                                html.th("ID Orden"),
                                html.th("Estado"),
                                html.th("Lista de Materiales"),
                                html.th("Fecha de Inicio"),
                                html.th("Fecha de Vencimiento")
                            )
                        ),
                        html.tbody(
                            {"style": {"textAlign": "center"}},
                            html.tr(
                                html.th({"scope": "row"}, "1"),
                                html.td(
                                    html.button(
                                        {"type": "button", "class": "btn", "style": {"color": "#000000", "backgroundColor": "#D0F4FF"}},
                                        html.b("Aprobado")
                                    )
                                ),
                                html.td("0957746KJLY"),
                                html.td("BOM-Rizz-0523-001"),
                                html.td("24/12/2020")
                            )
                        )
                    )
                )
            )
        )
    )


