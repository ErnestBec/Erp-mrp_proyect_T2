from reactpy import component, html



@component
def navbar_user():
    return(html.nav({"class":"navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"},
            html.button({"id":"sidebarToggleTop",
                        "class":"btn btn-link d-md-none rounded-circle mr-3"
                        },
            ),
            html.ul(
                {"class":"navbar-nav ml-auto"},
                html.li({"class":"nav-item dropdown no-arrow d-sm-none"}),
                html.div({"class":"topbar-divider d-none d-sm-block"}),
                html.li({"class":"nav-item dropdown no-arrow"},
                    html.a({"class":"nav-link dropdown-toggle"},
                        html.span({"class":"mr-2 d-none d-lg-inline text-gray-600 small"},"ADMINISTRADOR"),
                        html.img({"class":"img-profile rounded-circle", "src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/img/undraw_profile.svg"})
                    ),
                )
            )
            ))