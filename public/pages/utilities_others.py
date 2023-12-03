from reactpy import component, html
from components import  navbar2,nabvar_side, footer, navbar_user, card_icome, card_tasks, card_pending_request
from reactpy_router import link
from pages import home_page


@component
def utlities_oters():

    return html.div(
        html.div({
            "style": {
                "display": "flex",
            },
            "id": "page-top"
        },
            navbar2.NavbarTop(),
            html.div({"style": {
                "width": "100%"
            }, "id": "content-wrapper", "class": "d-flex flex-column"},
            html.div({"id": "content"},
                     html.div(navbar_user.navbar_user()),
                     html.div({"class": "container-fluid"},
                              html.h1({"class": "h3 mb-1 text-gray-800"},
                                      "Other Utilities"),
                              html.p(
                                  {"class": "mb-4"}, "Bootstrap's default utility classes can be found on the official"),
                              # Content Row
                              html.div({"class": "row"},
                                       html.div({"class": "col-lg-6"},
                                                # Overflow Hidden
                                                html.div({"class": "card mb-4"},
                                                         html.div({"class": "card-header py-3"},
                                                                  html.h6(
                                                             {"class": "m-0 font-weight-bold text-primary"}, "Overflow Hidden Utilty")
                                                ),
                                           html.div({"class": "card-body"}, "Use", html.code(
                                               ".o-hidde"), " to set the overflow property of any element to hidden.")


                                       ),
                                  # Progress Small
                                  html.div({"class": "card mb-4"},
                                           html.div({"class": "card-header py-3"},
                                                    html.h6(
                                               {"class": "m-0 font-weight-bold text-primary"}, "Progress Small Utility")
                                  ),
                                                    html.div({"class": "card-body"},
                                                             html.div(
                                                                 {"class": "mb-1 small"}, "Normal Progress Bar"),
                                                             html.div({"class": "progress mb-4"},
                                                                      html.div({"class": "progress-bar", "role": "progressbar", "style": "width: 75%",
                                                                               "aria-valuenow": "75", "aria-valuemin": "0", "aria-valuemax": "100"})
                                                                      ),
                                                             html.div(
                                                                 {"class": "mb-1 small"}, "Small Progress Bar"),
                                                             html.div({"class": "progress progress-sm mb-2"},
                                                                      html.div({"class": "progress-bar", "role": "progressbar", "style": "width: 75%",
                                                                               "aria-valuenow": "75", "aria-valuemin": "0", "aria-valuemax": "100"})

                                                                      ),
                                                             "Use the <code>.progress-sm</code> class along with <code>.progress</code>"



                                                             )

                                       ),
                                  # Dropdown No Arrow
                                  html.div({"class": "card mb-4"},
                                           html.div({"class": "card-header py-3"},
                                                    html.h6(
                                               {"class": "m-0 font-weight-bold text-primary"}, "Dropdown - No Arrow")
                                  ),
                                           html.div({"class": "card-body"},
                                                    html.div({"class": "dropdown no-arrow mb-4"},
                                                             html.button({"class": "btn btn-secondary dropdown-toggle", "type": "button", "id": "dropdownMenuButton", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                                                                         " Dropdown (no arrow)"

                                                                         ),
                                                             html.div({"class": "dropdown-menu", "aria-labelledby": "dropdownMenuButton"},
                                                                      html.a(
                                                                 {"class": "dropdown-item", "href": "#"}, "Action"),
                                                        html.a(
                                                                 {"class": "dropdown-item", "href": "#"}, "Another action"),
                                                        html.a(
                                                                 {"class": "dropdown-item", "href": "#"}, "Something else here"),

                                                    )
                                           ),
                                      "Add the <code>.no-arrow</code> class alongside the <code>.dropdown</code>"

                                  )
                                       )
                              ),
                         html.div({"class": "col-lg-6"},
                                  # Roitation Utilities
                                  html.div({"class": "card"},
                                           html.div({"class": "card-header py-3"},
                                                    html.h6(
                                               {"class": "m-0 font-weight-bold text-primary"}, "Rotation Utilities")
                                  ),
                             html.div({"class": "card-body text-center"},
                                      html.div(
                                 {"class": "bg-primary text-white p-3 rotate-15 d-inline-block my-4"}, ".rotate-15"),
                                      html.hr(),
                                      html.div(
                                 {"class": "bg-primary text-white p-3 rotate-n-15 d-inline-block my-4"}, ".rotate-n-15")

                                  )
                         )


                              )

                     )
            )

            ),

            footer.footer()

        )
        )


    )
