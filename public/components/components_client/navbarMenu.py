from reactpy import component, html

@component
def Navbar():
    navbar_style = {
        "backgroundColor": "white",
    }
    return html.ul(
        {"className": "navbar-nav sidebar sidebar-dark accordion", "id": "accordionSidebar", "style": navbar_style},
        html.a(
            {"href": "#", "className": "d-flex align-items-center justify-content-center"},
            html.div(
                {"className": "navbar-brand"},
                html.a(
                    {"class": "btn mx-3", "style": {"color": "black", "display": "flex", "alignItems": "center"}},
                    html.i({"class": "bi bi-cpu", "style": {"fontSize": "30px", "marginRight": "8px", "fill": "currentColor"}}),
                    html.b({"style": {"lineHeight": "1"}}, "ElectroniXpress"),
                ),
            ),
        ),
        html.div(
            {"className": "sidebar-heading", "style": {"textAlign": "center", "marginTop": "15%", "fontSize": "15px"}},
            html.p({"style": {"color": "black"}}, html.b("Menu Principal")),
        ),
        html.li(
            {"class": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"class": "bi bi-clipboard-data", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(html.a({"href": "#", "style": {"color": "black"}}, "Dashboard")),
        ),
        html.li(
            {"className": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-card-list", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(html.a({"href": "/User_Solicitudes", "style": {"color": "black"}}, "Solicitudes")),
        ),
        html.li(
            {"className": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-bag", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(html.a({"href": "/User_Catalogo", "style": {"color": "black"}}, "Catálogo")),
        ),
        html.li(
            {"className": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-cash", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(html.a({"href": "/User_Cuentas", "style": {"color": "black"}}, "Cuentas")),
        ),
 
        html.br(), html.br(), html.br(), html.br(), html.br(),

        html.hr({"className": "sidebar-divider my-0", "style": {"backgroundColor": "black", "marginTop": "11%"}}),
        html.div(
            html.li(
                {"className": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
                html.i({"className": "bi bi-people", "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(html.a({"href": "#", "style": {"color": "black"}}, "Usuarios")),
            ),
            html.li(
                {"className": "nav-item active", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
                html.i({"className": "bi bi-gear", "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(html.a({"href": "#", "style": {"color": "black"}}, "Ajustes")),
            ),
        ),
    )

