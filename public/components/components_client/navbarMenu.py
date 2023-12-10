from reactpy import component, html
from reactpy_router import link

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
            {"class": "nav-item active d-flex", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"class": "bi bi-clipboard-data", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(link("Dashboard",to="/User_Dashboard",**{"style": {"color": "black"},"class_name":"link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"})),
        ),
        html.li(
            {"className": "nav-item active d-flex", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-card-list", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(link("Solicitudes", to ="/User_Solicitudes",**{ "style": {"color": "black"},"class_name":"link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"})),
        ),
        html.li(
            {"className": "nav-item active d-flex", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-bag", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(link( "Catálogo",to="/User_Catalogo",**{"style": {"color": "black"},"class_name":"link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"})),
        ),
        html.li(
            {"className": "nav-item active d-flex", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
            html.i({"className": "bi bi-cash", "style": {"fontSize": "20px", "marginRight": "8px"}}),
            html.b(link("Cuentas",to ="/User_Cuentas", **{ "style": {"color": "black"},"class_name":"link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"} )),
        ),
 
        html.br(), html.br(), html.br(), html.br(), html.br(),

        html.hr({"className": "sidebar-divider my-0", "style": {"backgroundColor": "black", "marginTop": "11%"}}),
        html.div(
            html.li(
                {"className": "nav-item active d-flex", "style": {"marginLeft": "10%", "marginTop": "8%", "color": "#000000", "textAlign": "left"}},
                html.i({"className": "bi bi-gear", "style": {"fontSize": "20px", "marginRight": "8px"}}),
                html.b(link("Ajustes",to ="/User_Ajustes", **{ "style": {"color": "black"},"class_name":"link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"} )),
            ),
        ),
    )

