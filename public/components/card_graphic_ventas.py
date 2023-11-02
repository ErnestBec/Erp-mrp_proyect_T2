from reactpy import component, html
from reactpy_router import link


@component
def card_graphic_ventas():
    return (
        html.div(
            {"class": "col-xl-8 col-lg-7"},
            html.div({"class": "card shadow mb-4"},
                     html.div({"class": "card-header py-3 d-flex flex-row align-items-center justify-content-between"},
                              html.h6(
                                  {"class": "m-0 font-weight-bold text-primary"}, "Ventas"),
                              html.div({"class": "dropdown no-arrow"},
                              html.a(
                                  {"class": "dropdown-toggle", "role": "button", "id": "dropdownMenuLink",
                                   "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                                  html.i(
                                      {"class": "fas fa-ellipsis-v fa-sm fa-fw text-gray-400"}),
                              ),
                         html.div({"class": "dropdown-menu dropdown-menu-right shadow animated--fade-in", "aria-labelledby": "dropdownMenuLink"},
                                  html.div(
                             {"class": "dropdown-header"}, "Dropdown Header:"),
                                  link("Action", to="/", **
                                       {"class": "dropdown-item"}),
                                  link("Anoter action", to="/", **
                                       {"class": "dropdown-item"}),
                                  html.div({"class": "dropdown-divider"}),
                                  link("Something else here", to="/", **
                                       {"class": "dropdown-item"}),
                              )
                     ),
            ),

                html.div({"class": "card-body"},
                         html.div({"class": "chart-area"},
                                  html.canvas(
                                  {"id": "myAreaChart"})
                                  )
                         )
            )
        )
    )
