from reactpy import component, html
from components import navbar_top, navbarMenu, btnFilter, btnFilterDay
from reactpy_router import link


@component

def Page_Cuentas():
    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class_name": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda("Cuentas"),
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
                                    "style": {"margin-top": "5%", "margin-bottom": "5%"},
                                }, html.div({"class":"row"},
                                            html.div({"class":"col-auto me-auto", "style":{"color":"black"}}, 
                                                     html.h6({"class":"display-6"}, 
                                                             html.b("Cuentas")
                                                            )
                                                    )
                                        ),
                                    
                            ),html.div( {"class" :"card-body", "style" : {"margin-top":"0%"}},                                        #Contenedor para la grafica y botones
                                    html.div({"class":"container-fluid"}, #Contenedor de los botones
                                           html.div({"class":"row no-border-bottom"},
                                                    html.div({"class":"col-auto"}, 
                                                             html.div({"class":"btn-group"},
                                                                    btnFilterDay.btnFilterDay(),
                                                                    btnFilter.btnFilter()
                                                                    )
                                                            )
                                                )  
                                           
                                           ),
                                           html.div({"class":"table-responsive", "style" :{"margin-top" :"2%"}},
                                                    html.table({"className": "table", "id": "dataTable"},
                                                               html.thead(
                                                                    html.tr(
                                                                        html.th({"scope":""}), 
                                                                        html.th({"scope":"col", "children":"No"}),
                                                                        html.th({"scope":"col", "children":"Codigo*"}),
                                                                        html.th({"scope":"col", "children":"BOM No"}),
                                                                        html.th({"scope":"col", "children":"Planned Qty*"}),
                                                                        html.th({"scope":"col", "children":"Planned (Start Date) *"}),
                                ),
                            ),
                         html.tbody(
                        html.tr(
                        html.th({"scope":"row", "children":"1"}),
                        html.td({"children":"Mark"}),
                        html.td({"children":"Otto"}),
                        html.td({"children":"$300.00USD"}),
                        html.td({"children":""}),
                        html.td({"children":"20/11/2023"}),
                            ),
                            html.tr(
                        html.th({"scope":"row", "children":"2"}),
                        html.td({"children":"Jacob"}),
                        html.td({"children":"Thornton"}),
                        html.td({"children":"$100.00USD"}),
                        html.td({"children":"Holi"}),
                        html.td({"children":"20/11/2023"}),
                        ),
                        html.tr(
                        html.th({"scope":"row", "children":"3"}),
                        html.td({"children":"Larry the Bird"}),
                        html.td({"children":"@twitter"}),
                        html.td({"children":"$200.00USD"}),
                        html.td({"children":""}),
                        html.td({"children":"20/11/2023"}),
                        ),
                        ),
                        )

                                                    )

                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
