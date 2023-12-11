from reactpy import component, html, hooks
from components.components_client import navbar_top, navbarMenu,table_client,btnFilter,btnFilterDay
from reactpy_router import link
import requests
def generate_arr_data(data):
    list_data=[]
    for list_prod in data:
        products =[]
        products.append(list_prod["num_referencia"])
        products.append(f'${list_prod["importe"]}')
        products.append(list_prod["status"])
        products.append(list_prod["date_registration"])
        products.append(list_prod["date_pay"])

        list_data.append(products)
    return list_data

@component
def Page_Cuentas():
    url = "http://10.228.1.158:8001/"
    # token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InQxZXF1aXBvc0BnbWFpbC5jb20iLCJwYXNzd29yZCI6InQxZXF1aXBvczEyMzQ1IiwiZXhwIjoxNzAyMzQ0MzY1fQ.RFAYukZH0P0m7V0X-gYRPKrN6r-B8jnP3TiHfRYDgoU"
    tokenClient="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRpZXIyQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoicHpzMTIzNDUiLCJleHAiOjE3MDI0NzMzOTB9.1i15KprqJjfQfgU2oN1AoTzfB-KBqjNOw7H4qalwGCM"
    
    dataTable, set_dataTable = hooks.use_state({})
    dataTableMonth, set_dataTableMonth = hooks.use_state({})
    dataTableStatus , set_dataTableStatus=hooks.use_state([])
    # Ise state de tokens
    token, setToken = hooks.use_state("Ignore")

    filterMonth, setFilterMonth = hooks.use_state(False)
    filterStatus, setFilterStatus= hooks.use_state(False)
    totalAccounts, setTotalAccounts= hooks.use_state(True)

    def getToken():
        return html.script("var elemento = document.getElementById('token'); var item = localStorage.getItem('token'); if (item == null) { item = \"None\"; } elemento.value = item; elemento.dispatchEvent(new Event('keypress'));")
    
    def validarSesion(tkn):
        script = ""
        if tkn != "Ignore":
            script = ("localStorage.clear();window.location.href = \"/\";" if (tkn == "None") else "localStorage.clear();localStorage.setItem(\"token\", \""+tkn+"\");")   
        return html.script(script)
    def request_data():
        headers = {"Authorization": f"Bearer {tokenClient}"}
        response =  requests.get(url + "cuentacobrar", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_dataTable(datos)
    
    hooks.use_effect(request_data,[])

    def request_data_month(month):
        headers = {"Authorization": f"Bearer {tokenClient}"}
        if month == "13":
            response =  requests.get(url + "cuentacobrar", headers=headers)
            setFilterMonth(False)
            setFilterStatus(False)
            setTotalAccounts(True)
        else:
            response =   requests.get(url + f"cuentacobrar/date-month/{month}", headers=headers)
            setFilterMonth(True)
            setFilterStatus(False)
            setTotalAccounts(False)
        response.raise_for_status()
        datos = response.json()
        set_dataTableMonth(datos)

    def request_data_status(status):
        headers = {"Authorization": f"Bearer {tokenClient}"}
        if status == "Pendiente":
            response =   requests.get(url + f"cuentacobrar/status/pending", headers=headers)
        elif status == "Pagado":
            response =   requests.get(url + f"cuentacobrar/status/paid", headers=headers)
        else:
            response =  requests.get(url + "cuentacobrar", headers=headers)
        setFilterMonth(False)
        setFilterStatus(True)
        setTotalAccounts(False)
        response.raise_for_status()
        datos = response.json()
        set_dataTableStatus(datos)

    
    headers =["Numero de Referencia","Importe","Estatus","Fecha de Emisión","Fecha a Pagar"]
    options_dropdown = ["Ver todos","Pendiente","Pagado"]
    dataTableCP = dataTable
    arr_products = generate_arr_data(dataTableCP["all_acounts"] if dataTableCP and "all_acounts" in dataTableCP else [])
    arr_productsMonth = generate_arr_data(dataTableMonth["requests"] if dataTableCP and "requests" in dataTableMonth else [])
    arr_productsStatus = generate_arr_data(dataTableStatus["all_acounts"]  if dataTableCP and "all_acounts" in dataTableStatus else [])

    def ShowTables():
        if filterMonth:
            return table_client.TableClient(headers, arr_productsMonth)
        elif filterStatus:
            return table_client.TableClient(headers, arr_productsStatus)
        elif totalAccounts:
            return table_client.TableClient(headers, arr_products)
                        
                     
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
                                            btnFilterDay.btnFilterDay(request_data_month),
                                            btnFilter.btnFilter(options_dropdown, request_data_status),
                                            
                                        ),
                                    ),
                                ),
                            ),
                        ShowTables(),
                        ),
                    ),
                ),
            ),
        ),
    )
