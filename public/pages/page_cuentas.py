from reactpy import component, html
from components import navbar_top, navbarMenu, btnFilter, btnFilterDay, table
from reactpy_router import link


@component

def Page_Cuentas():

    
    opciones = [
        "Cuentas por cobrar",
        "Cuentas por pagar",

    ]

    columnas = [
        "",
        "No",
        "Num. Referencia*",
        "Importe",
        "Estatus",
        "Fecha de emision",
        "Fecha de pago"
    ]

    datos = [


    ]

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
                                }
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
                                                                    btnFilter.btnFilter(opciones)
                                                                    )
                                                            )
                                                )  
                                           
                                           ),
                                           html.div({"class":"table-responsive", "style" :{"margin-top" :"2%"}},
                                                    table.Tabla(columnas,datos)

                                                    )

                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
