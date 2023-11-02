from reactpy import component, html
from components import nabvar_side, footer, navbar_user, card_icome, card_tasks, card_pending_request
from reactpy_router import link
from pages import home_page


@component
def cards():
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
        html.title("PANEL ADMINISTRADOR"),
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
                         card_icome.card_income(
                    "primary", "Ingresos (Mensuales)", 40.000, "fas fa-calendar fa-2x text-gray-300"),
                                  card_icome.card_income(
                                      "success", "Ingresos (Anuales)", 215.000, "fas fa-dollar-sign fa-2x text-gray-300"),
                                  card_pending_request.card_pending_request(
                                      50),
                                  card_tasks.card_task(18)
                     ),
                html.div({"class": "row"},
                         html.div({"class": "col-lg-6"},
                                  html.div({"class": "card mb-4"},
                                           html.div({"class": "card-header"},
                                                    "Default Card Example"),
                                           html.div({"class": "card-body"},
                                                    "This card uses Bootstrap's default styling with no utility classes added. Global styles are the only things modifying the look and feel of this default card example.")
                                           ),
                                  html.div({"class": "card mb-4"},
                                           html.div({"class": "card-header py-3"},
                                                    html.h6(
                                               {"class": "m-0 font-weight-bold text-primary"}, "Basic Card Example")
                                  ),
                             html.div({"class": "card-body"},
                                      "The styling for this basic card example is created by using default Bootstrap utility classes. By using utility classes, the style of the card component can be easily modified with no need for any custom CSS!"

                                      )
                         ),
                ),
                                  html.div({"class": "col-lg-6"},
                                           html.div({"class": "card shadow mb-4"},
                                                    # card header -dropdown
                                                    html.div({"class": "card-header py-3 d-flex flex-row align-items-center justify-content-between"},
                                                             html.h6(
                                                        {"class": "m-0 font-weight-bold text-primary"}, "Dropdown Card Example"),
                                               html.div({"class": "dropdown no-arrow"},
                                                        html.a({"class": "dropdown-toggle", "href": "#", "role": "button", "id": "dropdownMenuLink", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                                                               html.i(
                                                            {"class": "fas fa-ellipsis-v fa-sm fa-fw text-gray-400"}),
                                               ),
                                                        html.div({"class": "dropdown-menu dropdown-menu-right shadow animated--fade-in", "aria-labelledby": "dropdownMenuLink"},
                                                                 html.div(
                                                            {"class": "dropdown-header"}, "Dropdown Header:"),
                                                   html.a(
                                                            {"class": "dropdown-item", "href": "#"}, "Action"),
                                                   html.a(
                                                            {"class": "dropdown-item", "href": "#"}, "Other Action"),
                                                   html.div(
                                                            {"class": "dropdown-divider"}),
                                                   html.a(
                                                            {"class": "dropdown-item", "href": "#"}, "Something else Here"),

                                               )
                                                    )

                                           ),
                                      # card body
                                      html.div({"class": "card-body"},
                                               " Dropdown menus can be placed in the card header in order to extend the functionality of a basic card. In this dropdown card example, the Font Awesome vertical ellipsis icon in the card header can be clicked on in order to toggle a dropdown menu."
                                               )

                                  ),
                    html.div({"class": "card shadow mb-4"},
                                      html.a({"href": "#collapseCardExample", "class": "d-block card-header py-3", "data-toggle": "collapse", "role": "button", "aria-expanded": "true", "aria-controls": "collapseCardExample"},
                                             html.h6(
                                          {"class": "m-0 font-weight-bold text-primary"}, "Collapsable Card Example")
                    ),
                                      html.div({"class": "collapse show", "id": "collapseCardExample"},
                                               html.div({"class": "card-body"},
                                               " This is a collapsable card example using Bootstrap's built in collapse functionality.", html.strong("Click on the card header"), "to see the card bodycollapse and expand!"))
                                  )

                )


                     ),

            ),

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
