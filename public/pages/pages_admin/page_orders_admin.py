from reactpy import component, html, hooks
from components.components_admin import navbar_top, navbarMenu, tabla, btnFilter, btnFilterDay
from reactpy_router import link
import json
import requests


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
            response = requests.get(url + "requests", headers=headers)
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
    if edo == "Aprobada":
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
    if edo == "Pendiente":
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

    opciones = [
        "Total",
        "Pendiente",
        "Aprobada",
        "Completada",
    ]

    columnas = [
        "",
        "id",
        "status",
        "date_req",
        "num_ref_solicitud",
        "date_approved",
        "date_delivery_expected",
        "date_delivery",
        "client.name",
        "client.email",
        "client.phone",
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
                                        html.div(
                                            {"class": "col-auto"},
                                            html.div(
                                                {"class": "btn-group"},
                                                btnFilterDay.btnFilterDay(),
                                                btnFilter.btnFilter(opciones),
                                            ),
                                        ),
                                    ),
                                ),
                                # tabla.Tabla(columnas, datos_api)
                                # print(datos_api),
                                #tabla.Tabla(columnas, datos_api),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
