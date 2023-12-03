from reactpy import component, html

@component
def NavbarTop():
    return html.div(
        html.nav(
            {"class": "navbar navbar-expand navbar-light bg-white topbar d-flex mb-3 static-top shadow"},
            html.a(
                {"href": "#", "class": "btn p-2 d-flex", "role": "button", "type": "button", "data-bs-toggle": "button", "style": {"color": "black", "margin-right": "50%"}},
                html.i({"class":"bi bi-0-square"}),
                html.h6(
                    {"class": "d-flex"},
                    html.b("Solicitudes")
                )
            ),
            html.form(
                {"class": "d-flex p-2", "role": "search", "style": {"width": "35%", "style": "background-color:white"}},
                html.input(
                    {"type": "email", "class": "form-control navbar-nav ml-auto", "id": "floatingInput", "placeholder": "Buscar ...", "aria-label": "Search"}
                ),
                html.a(
                    {"class": "nav-link dropdown-toggle", "href": "#", "id": "userDropdown", "role": "button", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                 
             
                )
            )
        )
    )

# Puedes usar NavbarTop() en tu aplicación ReactPy
