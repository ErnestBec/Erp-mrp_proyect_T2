from reactpy import component, html
from reactpy_router import link

#
@component
def navbar_user():
    return (html.nav({"class": "navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"},
                     html.button({"id": "sidebarToggleTop",
                                 "class": "btn btn-link d-md-none rounded-circle mr-3"
                                  },
                                 html.i({"class": "fa fa-bars"})
                                 ),
                     html.form({"class": "d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search"},
                               html.div({"class": "input-group"},
                                        html.div(
                                            {"class": "input-group-append"})
                                        )
                               ),
                     html.ul(
        {"class": "navbar-nav ml-auto"},
        html.li({"class": "nav-item dropdown no-arrow d-sm-none"},
                html.a({"class": "nav-link dropdown-toggle",
                        "href": "#", "id": "searchDropdown",
                        "role": "button", "data-toggle": "dropdown",
                                "aria-haspopup": "true", "aria-expanded": "false"},
                       html.i({"class": "fas fa-search fa-fw"})
                       ),
                # <!-- Dropdown - Messages -->
                html.div({"class": "dropdown-menu dropdown-menu-rightp-3 shadow animated--grow-in",
                          "aria-labelledby": "searchDropdown"},
                         html.form({"class": "form-inline mr-auto w-100 navbar-search"},
                                   html.div({"class": "input-group"},
                                            html.input({"class": "form-control bg-light border-0 small",
                                                        "placeholder": "Search for...",
                                                        "aria-label": "Search",
                                                        "aria-describedby": "basic-addon2"
                                                        }),
                                            html.div({"class": "input-group-append"},
                                                     html.button({"class": "btn btn-primary", "type": "button"},
                                                                 html.i(
                                                                 {"class": "fas fa-search fa-sm"})
                                                                 )
                                                     )
                                            )
                                   )
                         )
                ),
        html.div({"class": "topbar-divider d-none d-sm-block"}),
        # <!-- Nav Item - User Information -->
        html.li({"class": "nav-item dropdown no-arrow"},
                html.a({"class": "nav-link dropdown-toggle", "href": "#", "id": "userDropdown", "role": "button",
                        "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                       html.span(
                    {"class": "mr-2 d-none d-lg-inline text-gray-600 small"}, "ADMINISTRADOR"),
            html.img({"class": "img-profile rounded-circle",
                      "src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/img/undraw_profile.svg"})
        ),
            # <!-- Dropdown - User Information -->
            html.div({"class": "dropdown-menu dropdown-menu-right shadow animated--grow-in",
                      "aria-labelledby": "userDropdown"
                      },
                     html.a({"class": "dropdown-item", "href": "#"},
                            html.i(
                         {"class": "fas fa-user fa-sm fa-fw mr-2 text-gray-400"}), "PROFILE"
            ),
            html.a({"class": "dropdown-item", "href": "#"},
                   html.i(
                {"class": "fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"}), "SETTINGS"
            ),
            html.a({"class": "dropdown-item", "href": "#"},
                   html.i(
                {"class": "fas fa-list fa-sm fa-fw mr-2 text-gray-400"}), "ACTIVITY LOG"
            ),
            html.div({"class": "dropdown-divider"}),
            link(
                html.i(
                    {"class": "fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"}),
                "LOGOUT", to="/login", **{"class": "dropdown-item", "href": "#"}
            ),
        )
        )

    )
    ))
