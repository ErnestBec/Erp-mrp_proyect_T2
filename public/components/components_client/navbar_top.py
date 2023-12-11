from reactpy import component, html, hooks
from reactpy_router import link
import requests


@component
def NavbarBusqueda(titulo, icono):
    url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InQxZXF1aXBvc0BnbWFpbC5jb20iLCJwYXNzd29yZCI6InQxZXF1aXBvczEyMzQ1IiwiZXhwIjoxNzAyMzQ0MzY1fQ.RFAYukZH0P0m7V0X-gYRPKrN6r-B8jnP3TiHfRYDgoU"
    email = "tier2@gmail.com"
    list_notifications, setNotifications=hooks.use_state({})

    def request_data(event):
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.get(url + "notifications-pending", headers=headers)
        response.raise_for_status()
        datos = response.json()
        setNotifications(datos)
        print("se abrio notificaciones")

    
    def Mark_as_read(id_notification):
        headers = {"Authorization": f"Bearer {token}"}
        response =  requests.put(url + "update-status/"+id_notification, headers=headers)
        response.raise_for_status()
        datos = response.json()
        print(datos)

    def list_Notifications():
        notifications_user=[]
        print(len(list_notifications["notifications"]))
        # datos = list_notifications
        # notifications = list_notifications.get("notifications") if list_notifications else None
        # list_notifications["notifications"] if list_notifications and "notifications" in list_notifications else {"notifications":[]}
        for notification in list_notifications["notifications"]:
            notifications_user.append(html.li({"style":{"list-style":"none"}},html.div(html.p(notification["Mesaage"]),html.p(notification["_id"]),html.button({"class":"btn btn-primary","on_click":lambda event : Mark_as_read(notification["_id"])},"Marcar como leido",html.i({"class":"bi bi-check2-square me-1 ms-1"}))),html.hr()))
        return html.ul({"class":"text-body-secondary"}, *notifications_user)
    def show_notifications():
        if list_notifications:
            return list_Notifications()
        else:
            return "Cargando ..."
    return html.nav(
            {
                "class": "navbar ps-4 pe-2 navbar-light bg-white topbar d-flex mb-3 static-top shadow container-fluid", "style":{"width":"100%"}
            },
            html.a(
                {
                    "href": "#",
                    "class": "btn",
                    "role": "button",
                    "type": "button",
                    "data-bs-toggle": "button",
                    "style": {"color": "black", "marginRight": "50%"},
                },
                html.i({"className": icono, "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(titulo),
            ),
               html.div(
        html.button(
            {"class": "btn", "type": "button", "data-bs-toggle": "offcanvas", "data-bs-target": "#offcanvasRight", "aria-controls": "offcanvasRight","on_click":lambda event :request_data(event)},
              html.i(
                                        {
                                            "class": "bi bi-bell-fill",
                                            "style": {"fontSize": "22px", "color": "black", "margin-right":"10px"},
                                        }
                )
        ),
        html.div(
            {"class": "offcanvas offcanvas-end", "tabindex": "-1", "id": "offcanvasRight", "aria-labelledby": "offcanvasRightLabel"},
            html.div(
                {"class": "offcanvas-header"},
                html.h5({"class": "offcanvas-title", "id": "offcanvasRightLabel"}, "Notificaciones"),
                html.button({"type": "button", "class": "btn-close", "data-bs-dismiss": "offcanvas", "aria-label": "Close","on_click":lambda event :setNotifications({})})
            ),
            html.div(
                {"class": "offcanvas-body"},
                    show_notifications()
            )
        )
    )
        
    )
