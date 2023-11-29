from reactpy import html, component
from components import top_navbar, nabvar_side


@component
def order_page():
    return (html.div({"id": "page-top"},
                     html.div({"id": "wrapper"},
                              nabvar_side.navbar(),
                     html.div({"id": "content-wrapper", "class": "d-flex flex-column"},
                              top_navbar.navbar_top()
                              )

                              )

                     ))
