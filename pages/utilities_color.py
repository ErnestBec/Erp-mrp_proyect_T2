from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer

#
@component
def utilities_color():
    bootstrap_css = html.link({
        "rel": "stylesheet",
        "href": "https://elpatronhh.github.io/portfolio/bootstrap.min.css"
    })
    style_css = html.link({
        "href": "https://elpatronhh.github.io/portfolio/sb-admin-2.min.css",
        "rel": "stylesheet"
    })
    fontawesome = html.link({
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
    })
    head = html.div(
        html.meta({
            "charset": "utf-8"
        }),
        html.meta({
            "http-equiv": "X-UA-Compatible",
            "content": "IE=edge"
        }),
        html.meta({
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
        }),
        html.meta({
            "name": "description",
            "content": ""
        }),
        html.meta({
            "name": "author",
            "content": ""
        }),
        html.title("Colores"),
        html.link({
            "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
            "rel": "stylesheet"
        }),

    ),
    return html.div(
        bootstrap_css,
        style_css,
        fontawesome,
        head,
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
        ),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery/jquery.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/bootstrap/js/bootstrap.bundle.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery-easing/jquery.easing.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/sb-admin-2.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/chart.js/Chart.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
        html.script(
            {"src": "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})

    )
