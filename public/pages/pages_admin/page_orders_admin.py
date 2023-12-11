from reactpy import component, html, hooks
from components.components_admin import navbar_top, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link
import json
import requests

def Tabla(columnas, documentos):
    
    def generar_filas_tabla(documentos):
        filas_tabla = []
        for i, doc in enumerate(documentos):
            fila = [
                html.th({"scope": "row"}, str(i + 1)),
                *[generar_celda(doc, columna) for columna in columnas[1:]],
            ]
            filas_tabla.append(html.tr(*fila))
        return filas_tabla

    def generar_celda(doc, columna):
        if columna == "products":
            return html.td(generar_dropdown(doc.get(columna, [])))
        elif columna == "status":
            return html.td(Estado(doc.get(columna, "")))
        else:
            return html.td(obtener_valor(doc, columna))

    def generar_dropdown(products):
        options = [
            html.option(
                {"value": f"{prod['id_prod']}, {prod['quantity_missing']}"},
                f"{prod['id_prod']}, {prod['quantity_missing']}",
            )
            for prod in products
        ]
        return html.select(options)

    def obtener_valor(doc, columna):
        if "." in columna:
            atributos = columna.split(".")
            valor = doc
            for atributo in atributos:
                if isinstance(valor, dict) and atributo in valor:
                    valor = valor[atributo]
                elif isinstance(valor, list) and atributo.isdigit():
                    indice = int(atributo)
                    if indice < len(valor):
                        valor = obtener_valor(valor[indice], ".".join(atributos[2:]))
                    else:
                        valor = ""
                    break
                else:
                    valor = ""
                    break
        else:
            valor = doc.get(columna, "")
        return valor

    filas_tabla = generar_filas_tabla(documentos)

    tabla = html.table(
        {"class": "table", "id": "dataTable"},
        html.thead(
            {"style": "text-align: center;"},
            html.tr(*[html.th({"scope": ""}, encabezado) for encabezado in columnas]),
        ),
        html.tbody({"style": "text-align: center;"}, *filas_tabla),
    )

    contenedor_tabla = html.div(
        {"class": "table-responsive", "style": "margin-top: 2%;"}, tabla
    )
    return contenedor_tabla

def obtener_datos_api():
    url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
    mail = "tier2@gmail.com"
    pswd = "pzs12345"
    info = {"email": str(mail), "password": str(pswd)}

    response = requests.post(
        url + "login",
        data=json.dumps(info),
        headers={"Content-Type": "application/json"},
    )

    if response.status_code >= 200 and response.status_code < 300:
        token = str(response.json()["token"])

        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = requests.get(url + "admin/order-production", headers=headers)
            response.raise_for_status()
            datos = response.json()
            return datos
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error de conexión:", errc)
        except requests.exceptions.Timeout as errt:
            print("Tiempo de espera agotado:", errt)
        except requests.exceptions.RequestException as err:
            print("Error desconocido:", err)
    else:
        print(f"Error en la solicitud POST. Código de estado: {response.status_code}")

    return []

datos_api = obtener_datos_api()

def Estado(edo):
    if edo == "complete":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#AFF2FF",
                    "font-size": "14px",
                },
            },
            html.b(f"{edo}"),
        )
    if edo == "pending":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#F0FE88",
                    "font-size": "14px",
                },
            },
            html.b(f"{edo}"),
        )

    if edo == "Completada":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#5BDD4B",
                    "font-size": "14px",
                },
            },
            html.b(f"{edo}"),
        )

    if edo == "No Empezada":
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FF6060",
                    "font-size": "14px",
                },
            },
            html.b(f"{edo}"),
        )


@component
def Page_Ordenes():
    titulo = "Ordenes"

    icono = "bi bi-cart3"

    columnas_ad = [
        "",
        "_id",
        "fecha_alta",
        "products",
        "fecha_termino",
        "num_ref_solicitud",
        "status",
    ]

    return html.div(
        {"id": "app"},
        html.div(
            {"id": "wrapper"},
            navbarMenu.Navbar(),
            html.div(
                {"id": "content-wrapper", "class": "d-flex flex-column"},
                html.div(
                    {"id": "content"},
                    navbar_top.NavbarBusqueda(titulo, icono),
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
                                            html.b("Ordenes Totales"),
                                        ),
                                    ),
                                ),
                                html.div(
                                    {"class": "row"},
                                    html.div(
                                        {"class": "col-auto me-auto"},
                                        html.p(
                                            {
                                                "class": "display-8",
                                                "style": "color: black;",
                                            },
                                            "Estás viendo el número total de ordenes realizadas hasta el momento",
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
                                    ),
                                ),
                                Tabla(columnas_ad, datos_api)
                                # print(datos_api),
                                #tabla.Tabla(columnas, datos_api),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
