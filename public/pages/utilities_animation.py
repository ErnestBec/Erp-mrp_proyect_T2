from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer


@component
def utilities_animation():

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
                             html.div({"class": "container.fluid"},
                                      html.div({"class": "row"},
                                               html.div({"clas": "col-lg-6"},
                                                        html.div({"class": "card position-relative"},
                                                                 html.div({"class": "card-header py-3"},
                                                                          html.h6(
                                                                     {"class": "m-0 font-weight-bold text-primary"}, "Grow In Animation Utilty")
                                                        ),
                                                   html.div({"class": "card-body"},
                                                            html.div({"class": "mb-3"},
                                                                     html.code(
                                                                {".animated--grow-in"})
                                                   ),
                                                            html.div(
                                                       {"class": "small mb-1"}, "Navbar Dropdown Example:"),
                                                            html.nav({"class": "navbar navbar-expand navbar-light bg-light mb-4"},
                                                                     html.a(
                                                                {"class": "navbar-brand", "href": "#"}, "Navbar"),
                                                       html.ul({"class": "navbar-nav ml-auto"},
                                                               html.li({"class": "nav-item dropdown"},
                                                                       html.a({"class": "nav-link dropdown-toggle", "href": "#", "id": "navbarDropdown",
                                                                               "role": "button", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}, "Dropdown"),
                                                                       html.div({"class": "dropdown-menu dropdown-menu-right animated--grow-in",
                                                                                 "aria-labelledby": "navbarDropdown"},
                                                                                html.a(
                                                                           {"class": "dropdown-item", "href": "#"}, "Action"),
                                                                   html.a(
                                                                           {"class": "dropdown-item", "href": "#"}, "Another action"),
                                                                   html.div(
                                                                           {"class": "dropdown-divider"}),
                                                                   html.a(
                                                                           {"class": "dropdown-item", "href": "#"}, "Something else here")
                                                               ),
                                                       ),
                                                            ),
                                                   ),
                                                        ),
                                               ),
                                      ),
                                 html.div({"class": "col-lg-6"},
                                          html.div({"class": "card position-relative"},
                                                   html.div({"class": "card-header py-3"},
                                                            html.h6(
                                                       {"class": "m-0 font-weight-bold text-primary"}, "Fade In Animation Utilty")
                                          ),
                                     html.div({"class": "card-body"},
                                              html.div({"class": "mb-3"},
                                                       html.code(
                                                  {".animated--fade-in"})
                                     ),
                                              html.div(
                                         {"class": "small mb-1"}, "Navbar Dropdown Example:"),
                                              html.nav({"class": "navbar navbar-expand navbar-light bg-light mb-4"},
                                                       html.a(
                                                  {"class": "navbar-brand", "href": "#"}, "Navbar"),
                                         html.ul({"class": "navbar-nav ml-auto"},
                                                 html.li({"class": "nav-item dropdown"},
                                                         html.a({"class": "nav-link dropdown-toggle", "href": "#", "id": "navbarDropdown",
                                                                 "role": "button", "data-toggle": "dropdown", "aria-haspopup": "true",
                                                                 "aria-expanded": "false"}, "Dropdown"),
                                                         html.div({"class": "dropdown-menu dropdown-menu-right animated--fade-in",
                                                                   "aria-labelledby": "navbarDropdown"},
                                                                  html.a(
                                                             {"class": "dropdown-item", "href": "#"}, "Action"),
                                                     html.a(
                                                             {"class": "dropdown-item", "href": "#"}, "Another action"),
                                                     html.div(
                                                             {"class": "dropdown-divider"}),
                                                     html.a(
                                                             {"class": "dropdown-item", "href": "#"}, "Something else here")
                                                 ),
                                         ),
                                              ),
                                     ),
                                              html.div(
                                         {"class": "small mb-1"}, "Dropdown Button Example:"),
                                              html.div({"class": "dropdown mb-4"},
                                                       html.button({"class": "btn btn-primary dropdown-toggle", "type": "button",
                                                                    "id": "dropdownMenuButton", "data-toggle": "dropdown", "aria-haspopup": "true",
                                                                    "aria-expanded": "false"}, "dropdown"),
                                                       html.div({"class": "dropdown-menu animated--fade-in",
                                                                 "aria-labelledby": "dropdownMenuButton"},
                                                                html.a(
                                                           {"class": "dropdown-item", "href": "#"}, "Action"),
                                                  html.a(
                                                           {"class": "dropdown-item", "href": "#"}, "Another action"),
                                                  html.a(
                                                           {"class": "dropdown-item", "href": "#"}, "Something else here")
                                              ),
                                     ),

                                          ),
                                 ),
                                      ),
                             ),

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
