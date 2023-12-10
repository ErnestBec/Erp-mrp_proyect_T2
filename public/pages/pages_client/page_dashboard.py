from reactpy import  component, html
from components.components_client import navbar_top, navbarMenu,table_client,btnFilter,btnFilterDay
from reactpy_router import link


@component
def page_user_Dashboard():
    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class_name": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda("Cuentas por pagar", "bi bi-coin"),
                    html.div(
                        {"class_name": "container-fluid"},
                        html.div(
                            {
                                "class": "card sh adow mb-4",
                                "style": {
                                    "background-color": "white",
                                    "border-radius": "10px",
                                },
                            },
                            html.div(
                                {
                                    "class": "container-fluid",
                                    "style": {"margin-top": "5%"},
                                },
                                html.h5(
                                    {"class": "display-6", "style": {"color": "black"}},
                                    "Cuentas",
                                ),
                                html.h6(
                                    "Listado de Cuentas por pagar",
                                ),
                            ),
                            html.div(
                                {"class": "container-fluid"},
                                html.div(
                                    {"class": "row no-border-bottom"},
                                    html.div(
                                        {"class": "col-auto"},
                                        html.div(
                                            {"class": "btn-group mt-4 mb-4"},
                                            # btnFilterDay.btnFilterDay( request_data_month),
                                            # btnFilter.btnFilter(options_dropdown, request_data_status),
                                            
                                        ),
                                    ),
                                ),
                            ),
                        # ShowTables(),
                        ),
                    ),
                ),
            ),
        ),
    )
