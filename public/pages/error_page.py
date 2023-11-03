from reactpy import component, html
from components import nabvar_side, footer, navbar_user
from reactpy_router import link


@component
def error():

    return (
        html.div(
            html.div({"id": "page-top"},
                     html.div({"id": "wrapper"},
                              html.ul({"class": "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion", "id": "accordionSidebar"},
                                      html.a(link(html.div({"class": "sidebar-brand-icon rotate-n-15"},
                                                           html.i(
                                                               {"class": "fas fa-laugh-wink"})
                                                           ),
                                                  html.div({"class": "sidebar-brand-text mx-3"},
                                                           "SB ADMIN", html.sup("2")),
                                                  to="/login", **{"class": "sidebar-brand d-flex align-items-center justify-content-center"}),
                                             ),
                                      html.hr(
                                          {"class": "sidebar-divider my-0"}),
                                      html.div(
                                          {"class": "sidebar-heading"}, "Addons"),
                                      html.li({"class": "nav-item active"},
                                              html.a({"class": "nav-link", "href": "#", "data-toggle": "collapse", "data-target": "#collapsePages", "aria-expanded": "true", "aria-controls": "collapsePages"},
                                                     html.i(
                                                  {"class": "fas fa-fw fa-folder"}),
                                          html.span("Pages")),
                                  html.div({"id": "collapsePages", "class": "collapse show", "aria-labelledby": "headingPages", "data-parent": "#accordionSidebar"},
                                           html.div({"class": "bg-white py-2 collapse-inner rounded"},
                                                    html.h6(
                                               {"class": "collapse-header"}, "Login Screens"),
                                      html.a(
                                               link("login", to="/login", **{"class": "collapse-item"}))

                                  )

                                          )
                              ),
                     ),
                html.div({"class": "container-fluid"},
                         html.div({"class": "text-center"},
                                  html.div(
                             {"class": "error mx-auto", "data-text": "404"}, "404"),
                    html.p(
                             {"class": "lead text-gray-800 mb-5"}, "Page Not Found"),
                    html.p(
                             {"class": "text-gray-500 mb-0"}, "It looks like you found a glitch in the matrix..")
                )),
            ),
                footer.footer(),

            )

        )


    )
