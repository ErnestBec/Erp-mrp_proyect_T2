from reactpy import  component, html, hooks
from components.components_client import navbar_top, navbarMenu,table_client,btnFilter,btnFilterDay
from reactpy_router import link
import requests
def generate_arr_data(data):
    list_data=[]
    for list_prod in data:
        products =[]
        products.append(list_prod["num_ref_solicitud"])
        products.append(list_prod["status"])
        products.append(list_prod["date_req"])
        products.append(list_prod["date_delivery_expected"])
        products.append(list_prod["date_delivery"])
        list_data.append(products)
    return list_data

@component
def page_user_Dashboard():

    url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InQxZXF1aXBvc0BnbWFpbC5jb20iLCJwYXNzd29yZCI6InQxZXF1aXBvczEyMzQ1IiwiZXhwIjoxNzAyMzQ0MzY1fQ.RFAYukZH0P0m7V0X-gYRPKrN6r-B8jnP3TiHfRYDgoU"
    # tablas de Resumen de solicitudes
    dataTable, set_dataTable = hooks.use_state({})
    dataTableMonth, set_dataTableMonth = hooks.use_state({})
    dataTableStatus , set_dataTableStatus=hooks.use_state([])

    # Tablas de Deudas Pendientes y Completadas
    dataTableDeudas, seDataTableDeudas = hooks.use_state({})
    
    # Ise state de tokens
    token, setToken = hooks.use_state("Ignore")
    # tablas de Resumen de solicitudes
    filterMonth, setFilterMonth = hooks.use_state(False)
    filterStatus, setFilterStatus= hooks.use_state(False)
    totalAccounts, setTotalAccounts= hooks.use_state(True)

    def request_data():
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(url + "requests", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_dataTable(datos)
    
    hooks.use_effect(request_data,[])

    def request_data_month(month):
        headers = {"Authorization": f"Bearer {token}"}
        if month == "13":
            response =  requests.get(url + "requests", headers=headers)
            setFilterMonth(False)
            setFilterStatus(False)
            setTotalAccounts(True)
        else:
            response =   requests.get(url + f"request/date-mont/{month}", headers=headers)
            setFilterMonth(True)
            setFilterStatus(False)
            setTotalAccounts(False)
        response.raise_for_status()
        datos = response.json()
        set_dataTableMonth(datos)

    def request_data_status(status):
        headers = {"Authorization": f"Bearer {token}"}
        if status == "Pendiente":
            response =   requests.get(url + f"requests/status/pending", headers=headers)
        elif status == "Completado":
            response =   requests.get(url + f"requests/status/complete", headers=headers)
        else:
            response =  requests.get(url + "requests", headers=headers)
        setFilterMonth(False)
        setFilterStatus(True)
        setTotalAccounts(False)
        response.raise_for_status()
        datos = response.json()
        set_dataTableStatus(datos)

    
    headers =["Numero de Referencia","Estatus","Fecha de Emisión","Fecha de Esperada","Fecha a Entregar"]
    options_dropdown = ["Ver todos","Pendiente","Completado"]
    dataTableCP = dataTable
    arr_products = generate_arr_data(dataTableCP)
    arr_productsMonth = generate_arr_data(dataTableMonth["requests"] if dataTableCP and "requests" in dataTableMonth else [])
    arr_productsStatus = generate_arr_data(dataTableStatus)
    
    
    def ShowTables():
        if filterMonth:
            return table_client.TableClient(headers, arr_productsMonth)
        elif filterStatus:
            return table_client.TableClient(headers, arr_productsStatus)
        elif totalAccounts:
            return table_client.TableClient(headers, arr_products)
    # def showTablesCuentas()
        ""                  
    
    def getToken():
        return html.script("var elemento = document.getElementById('token'); var item = localStorage.getItem('token'); if (item == null) { item = \"None\"; } elemento.value = item; elemento.dispatchEvent(new Event('keypress'));")
    
    def validarSesion(tkn):
        script = ""
        if tkn != "Ignore":
            script = ("localStorage.clear();window.location.href = \"/\";" if (tkn == "None") else "localStorage.clear();localStorage.setItem(\"token\", \""+tkn+"\");")   
        return html.script(script)
    
    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.input({"style":"display : none", "id":"token", "onkeypress":lambda event: setToken(str(event['currentTarget']['value'] ))}),
            getToken(),
            validarSesion(token),
                                    html.div(
                {"id": "content-wrapper", "class_name": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda("Panel de Usuario", "bi bi-coin"),
                    html.div(
                        {"class_name": "container-fluid"},
                        html.div(
                            {
                                "class": "card sh adow  ",
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
                                    "Panel de Usuario",
                                ),
                                html.h6(
                                    "Resumen de su actividad",
                                ),
                            ),
                            html.div(
                                {"class": "container-fluid"},
                                html.div(
                                {
                                    "class": "container-fluid",
                                    "style": {"margin-top": "1%"},
                                },
                                html.h5(
                                    {"class": "display-6", "style": {"color": "black"}},
                                    "Resumen de solicitudes",
                                ),
                                html.h6(
                                    "Resumen de solicitudes",
                                ),
                            ),
                                html.div(
                                    {"class": "row no-border-bottom"},
                                    html.div(
                                        {"class": "col-auto"},
                                        html.div(
                                            {"class": "btn-group mt-4 mb-4"},
                                            btnFilterDay.btnFilterDay( request_data_month),
                                            btnFilter.btnFilter(options_dropdown, request_data_status),
                                        ),
                                    ),
                                ),
                            ),
                                            ShowTables(),

                            html.div(
                                {"class": "container-fluid"},
                                html.div(
                                {
                                    "class": "container-fluid",
                                    "style": {"margin-top": "5%"},
                                },
                                html.h5(
                                    {"class": "display-6", "style": {"color": "black"}},
                                    "Graficos de Deudas",
                                ),
                                html.h6(
                                    "Muestra el total de dedudas pendientes y pagadas",
                                ),
                            ),
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
                            html.div(
        html.canvas({"id":"myChart"})
    ),
                            html.div(
                                {"class": "container-fluid"},
                                html.div(
                                {
                                    "class": "container-fluid",
                                    "style": {"margin-top": "5%"},
                                },
                                html.h5(
                                    {"class": "display-6", "style": {"color": "black"}},
                                    "Deudas pentientes y Completadas",
                                ),
                                html.h6(
                                    "Resumen de Pagos",
                                ),
                            ),
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
