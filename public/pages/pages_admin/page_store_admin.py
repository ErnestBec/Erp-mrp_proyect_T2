from reactpy import component, html
from components.components_admin import navbar_top, navbarMenu, tabla
from reactpy_router import link
import json
import requests


def Tabla(columnas, response_body):

    if isinstance(response_body, dict):
        documentos = response_body.get("warehouses", [])
    else:
        documentos = json.loads(response_body).get("warehouses", [])

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
        if columna == "list_mp":
            return html.td(generar_dropdown(doc.get(columna, [])))
        elif columna == "capacity":
            return html.td(Capacidad(doc.get(columna, "")))
        else:
            return html.td(obtener_valor(doc, columna))

    def generar_dropdown(products):
        options = [
            html.option(
                {"value": f"{prod['id_mp']}, {prod['order_quantity']}"},
                f"{prod['id_mp']}, {prod['order_quantity']}",
            )
            for prod in products
        ]
        return html.select(options)

    def obtener_valor(doc, columna):
        if isinstance(doc, dict):
            if "." in columna:
                atributos = columna.split(".")
                valor = doc
                for atributo in atributos:
                    if isinstance(valor, dict) and atributo in valor:
                        valor = valor[atributo]
                    elif isinstance(valor, list) and atributo.isdigit():
                        indice = int(atributo)
                        if indice < len(valor):
                            valor = obtener_valor(
                                valor[indice], ".".join(atributos[1:])
                            )
                        else:
                            valor = ""
                        break
                    else:
                        valor = ""
                        break
            else:
                valor = doc.get(columna, "")
            return valor
        else:
            return ""

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
            response = requests.get(url + "admin/warehouse/capacity", headers=headers)
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


def Capacidad(cap):
    if 0 <= cap <= 9:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#F0FFA5",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )
    if 10 <= cap <= 29:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFD6A5",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )
    if 30 <= cap <= 49:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFBA67",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )
    if 50 <= cap <= 69:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FFEA67",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )
    if 70 <= cap <= 89:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#CAF365",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )
    if 90 <= cap <= 100:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#50C242",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )

    if cap > 100:
        return html.button(
            {
                "type": "button",
                "class": "btn",
                "style": {
                    "color": "#000000",
                    "background-color": "#FF0000",
                    "font-size": "14px",
                },
            },
            html.b(f"{cap}%"),
        )


@component
def Page_Almacenes():
    titulo = "Almacenes"

    icono = "bi bi-database"

    columnas = ["", "id_warehouse", "name_stock", "capacity", "date_update"]

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
                                            html.b("Almacenes"),
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
                                            "Monitoreo de capacidad",
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
                                Tabla(columnas, datos_api),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
