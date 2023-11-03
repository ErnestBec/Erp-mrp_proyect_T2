from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer


@component
def utilities_color():

    return html.div(

        html.div({
            "style": {
                "display": "flex",
            },
            "id": "page-top"
        },
            nabvar_side.navbar(),
            html.div({"style": {
                "width": "100%"
            }, "id": "content-wrapper", "class": "d-flex flex-column"},
                html.div({"id": "content"},
                         html.div(navbar_user.navbar_user()),
                         html.div({"class": "container-fluid"},
                                  html.div({"class": "d-sm-flex align-items-center justify-content-between mb-4"},
                                           html.h1(
                                      {"class": "h3 mb-0 text-gray-800"}, "Dashboard"),
                                      html.a({"class": "d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"},
                                             html.i(
                                                 {"class": "fas fa-download fa-sm text-white-50 me-2"}), "Reporte de Ventas"
                                             )
                         ),
                    html.div({"class": "row d-flex"},
                             html.div({"id": "wrapper"},
                                      html.ul({"class": "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion", "id": "accordionSidebar"},
                                              html.a({"class": "sidebar-brand d-flex align-items-center justify-content-center", "href": "index.html"},
                                                     html.div({"class": "sidebar-brand-icon rotate-n-15"},
                                                              html.i(
                                                         {"class": "fas fa-laugh-wink"})
                                              ),
                                          html.div({"class": "sidebar-brand-text mx-3"},
                                                   "SB Admin",
                                                   html.sup("2")
                                                   )
                                      ),
                                 html.hr(
                                          {"class": "sidebar-divider my-0"}),
                                 html.div(
                                          {"class": "sidebar-heading"}, "interface"),
                                 html.li({"class": "nav-item"},
                                         html.a({"class": "nav-link collapsed", "href": "#", "data-toggle": "collapse", "data-target": "#collapseTwo",
                                                 "aria-expanded": "true", "aria-controls": "collapseTwo"},
                                                html.i(
                                             {"class": "fas fa-fw fa-cog"}),
                                     html.span({"Componentes"})
                                 ),
                                          html.div({"id": "collapseTwo", "class": "collapse", "aria-labelledby": "headingTwo", "data-parent": "#accordionSidebar"},
                                                   html.div({"class": "bg-white py-2 collapse-inner rounded"},
                                                            html.h6(
                                                       {"class": "collapse-header"}, "Componentes personalizados:"),
                                              html.a(
                                                       {"class": "collapse-item", "href": "buttons.html"}, "Botones"),
                                              html.a({"class": "collapse-item",
                                                      "href": "cards.html"}, "Tarjetas")
                                          )
                                 )
                                      ),
                                 html.li({"class": "nav-item active"},
                                         html.a({"class": "nav-link", "href": "#", "data-toggle": "collapse", "data-target": "#collapseUtilities",
                                                 "aria-expanded": "true", "aria-controls": "collapseUtilities"},
                                                html.i(
                                             {"class": "fas fa-fw fa-wrench"}),
                                     html.span({"Utilidades"})
                                 ),
                                          html.div({"id": "collapseUtilities", "class": "collapse show", "aria-labelledby": "headingUtilities",
                                                   "data-parent": "#accordionSidebar"},
                                                   html.div({"class": "bg-white py-2 collapse-inner rounded"},
                                                            html.h6({"class": "collapse-header"},
                                                                    "Utilidades personalizadas:")
                                                            )
                                                   )
                                      )

                             )
                    )
                         )
                    # html.div(componentes.login_user())
                ),
                    html.div()
            ),
                footer.footer()

        )
        )
    )
