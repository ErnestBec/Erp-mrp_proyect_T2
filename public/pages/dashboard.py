from reactpy import component, html
from components import navbar_top, navbarMenu, btnFilter, btnFilterDay, table, chart, card_graphic_ventas
from reactpy_router import link

@component
def Dashboard():
    titulo = "Dashboard"

    icono = "bi bi-clipboard-data"

    opciones = [
        "Ordenes Totales",
        "Ordenes Pendientes",
        "Ordenes Aprobadas",
        "Ordenes Completadas",
    ]

    opciones2 = [
        "Totales",
        "Pendientes",
        "Aprobadas",
        "Completadas",
    ]

    columnas2 = [
        "No",
        "ID Orden*",
        "Descripcion",
        "Cantidad",
        "Estatus",
        "Fecha"
    ]

    datos2=[

    ]

    columnas = [
        "",
        "Cliente",
        "ID Orden",
        "Estado",
        "Estado del Inventario",
        "Fecha",
    ]
    datos =[


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
                    navbar_top.NavbarBusqueda(titulo, icono),
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
                                                             html.b("Ordenes Recientes")
                                                            )
                                                    )
                                        ),
                                    html.div({"class":"row"},
                                              html.div({"class":"col-auto me-auto", "style":{"color":"black"}}, 
                                                     html.p("Listado de todas las ordenes")
                                                    )
                                             )
                                    
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

                    html.div( {"class_name": "container-fluid"},#Contenedo de la grafica
                        html.div(
                            {
                                "class": "card sh adow mb-4",
                                "style": {
                                    "background-color": "white",
                                    "border-radius": "10px",
                                }
                            },
                            html.div({
                                        "class": "container-fluid",
                                        "style": {"margin-top": "5%", "margin-bottom": "5%"}}, 
                                        html.div({"class":"row"},
                                            html.div({"class":"col-auto me-auto", "style":{"color":"black"}}, 
                                                     html.h6({"class":"display-6"}, 
                                                             html.b("Graficas")
                                                            )
                                                    )
                                        ),
                                        html.div({"class":"container-fluid"},
                                                 definirGrafica("Grafica de Pantallas")
                                                 )
                                                                       
                                    ),
                        ),
                    ),

                    html.div( #Contenedor del inventario
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
                                                             html.b("Inventario de solicitudes")
                                                            )
                                                    )
                                        ),
                                    html.div({"class":"row"},
                                              html.div({"class":"col-auto me-auto", "style":{"color":"black"}}, 
                                                     html.p("Se muestra un listado de todas las solicitudes que se esperan por aprobar")
                                                    )
                                             )
                                    
                            ),html.div( {"class" :"card-body", "style" : {"margin-top":"0%"}},                                        #Contenedor para la grafica y botones
                                    html.div({"class":"container-fluid"}, #Contenedor de los botones
                                           html.div({"class":"row no-border-bottom"},
                                                    html.div({"class":"col-auto"}, 
                                                             html.div({"class":"btn-group"},
                                                                    btnFilterDay.btnFilterDay(),
                                                                    btnFilter.btnFilter(opciones2)
                                                                    )
                                                            )
                                                )  
                                           
                                    ),
                                    html.div({"class":"table-responsive", "style" :{"margin-top" :"2%"}},
                                                    table.Tabla(columnas2,datos2)

                                                    )

                            ),
                        ),
                    )
                ),
            ),
        ),
    )

    
def definirGrafica(dash):
    longitudx = ["1", "2", "3", "4","5"]
    titulo = "Venta de piezas"
    color= "#00BA34"
    datos = [54152645,51254559,5645512,564865,8456156,984561]
    nombre = "Pantalla"
    graficas = []
    graficas.append(chart.newChart(nombre, datos, color))
    
    strCharts = "["
    for i in graficas:
        strCharts+=(i+",")
    strCharts+="]"

    return card_graphic_ventas.linearChartComponent(str(dash), (str(longitudx)), titulo, strCharts)





    

