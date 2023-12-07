import reactpy
import requests
import json
import requests
import json
from reactpy import component, hooks, html, run


@reactpy.component
def Tabla(datos):
    return reactpy.html.table(
        reactpy.html.thead(
            reactpy.html.tr(
                reactpy.html.th("ID Request"),
                reactpy.html.th("Importe"),
                reactpy.html.th("Fecha de Pago"),
            )
        ),
        reactpy.html.tbody(
            *[
                reactpy.html.tr(
                    reactpy.html.td(str(dato["id_request"]["$oid"])),
                    reactpy.html.td(dato.get("importe", "")),
                    reactpy.html.td(dato.get("date_issue", "")),
                    reactpy.html.td(dato.get("date_pay", "")),
                )
                for dato in datos
            ]
        ),
    )



@component
def App():
    # Estado para almacenar la cantidad de peticiones realizadas
    request_count, set_request_count = hooks.use_state(0)
    max_requests = 5  # Límite de peticiones

    url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
    mail = "tier2@gmail.com"
    pswd = "pzs12345"
    info = {"email": str(mail), "password": str(pswd)}
    result = ""
    link = ""

    # Verificar si se supera el límite de peticiones
    if request_count < max_requests:
        response = requests.post(
            url + "login",
            data=json.dumps(info),
            headers={"Content-Type": "application/json"},
        )

        if response.status_code >= 200 and response.status_code < 300:
            token = str(response.json()["token"])
            print(token)

            headers = {'Authorization': f'Bearer {token}'}

            try:
                # Incrementar el estado de la cantidad de peticiones realizadas
                set_request_count(request_count + 1)

                response = requests.get(url + "type_warehouse_materials", headers=headers)
                response.raise_for_status()
                datos = response.json()
            except Exception as e:
                print("Error al obtener datos:", e)
                datos = []

    # Renderizar el contenido, incluyendo la cantidad de peticiones realizadas
    return datos
