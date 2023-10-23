from reactpy import component, html
from reactpy_router import link


@component
def card_grpahic_round():
    return (
        html.div({"class": "col-xl-4 col-lg-5"},
                 html.div({"class": "card shadow mb-4"},
                          html.div({"class": "card-header py-3 d-flex flex-row align-items-center justify-content-between"},
                                   html.h6(
                                       {"class": "m-0 font-weight-bold text-primary"}, "Ordenes"),
                                   html.div({"class": "dropdown no-arrow"},
                                            html.a({"class": ""}, html.i({"class": "dropdown-toggle", "role": "button", "id": "dropdownMenuLink",
                                                                          "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"})),
                                            html.div()
                                            )
                                   ),
                          html.div()

                          )
                 )
    )
