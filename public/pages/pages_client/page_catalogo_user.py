from reactpy import component, html, hooks
from components.components_client import navbar_top, navbarMenu,table_client
from reactpy_router import link
import json
import requests
def generate_arr_data(data):
    list_data=[]
    for list_prod in data:
        products =[]
        products.append(list_prod["id"])
        products.append(list_prod["name_prod"])
        products.append(list_prod["Descripcion"])
        products.append(f'${list_prod["precio_uni"]}')
        list_data.append(products)
    return list_data

@component
def Page_Catalogo():
    url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InQxZXF1aXBvc0BnbWFpbC5jb20iLCJwYXNzd29yZCI6InQxZXF1aXBvczEyMzQ1IiwiZXhwIjoxNzAyMzQ0MzY1fQ.RFAYukZH0P0m7V0X-gYRPKrN6r-B8jnP3TiHfRYDgoU"
    dataTable, set_dataTable = hooks.use_state([])
    def request_data():
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url + "products-user", headers=headers)
        response.raise_for_status()
        datos = response.json()
        set_dataTable(datos)
    hooks.use_effect(request_data,[])
    headers =["Id Producto","Nombre del Producto","Descripcion","Precio Unitario"]
    arr_products = generate_arr_data(dataTable)

    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda("Catálogo", "bi bi-bag"),
                    html.div(
                        {"class": "container-fluid"},
                        html.div(
                            {
                                "class": "card shadow mb-4",
                                "style": "background-color: white; border-radius:10px;",
                            },
                            html.div(
                                {
                                    "class": "container-fluid",
                                    "style": "margin-top: 5%; margin-bottom: 5%; color: #E8E8E8;",
                                },
                                html.div(
                                    {"class": "row"},
                                    html.div(
                                        {"class": "col-auto me-auto"},
                                        html.h6(
                                            {
                                                "class": "display-6",
                                                "style": "color: black;",
                                            },
                                            html.b("Catálogo"),
                                        ),
                                    ),
                                ),
                            ),
                            html.hr(
                                {
                                    "class": "sidebar-divider my-0",
                                    "style": "background-color: black; margin-top: 2%;",
                                }
                            ),
                            html.div(
                                {"class": "card-body", "style": "margin-top: 0%;"},
                                html.hr({"class": "sidebar-divider my-0"}),
                                html.div(
                                    {"class": "container-fluid"},
                                    html.div(
                                        {"class": "row no-border-bottom"},
                                        html.div(
                                            {"class": "col-auto"},
                                            html.div(
                                                {"class": "btn-group"},
                                                
                                            ),
                                        ),
                                    ),
                                ),
                                table_client.TableClient(headers,arr_products),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
