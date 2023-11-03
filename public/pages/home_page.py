from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer, card_graphic_ventas, card_graphic_round


@component
def home_page():
    return html.div({
        "id": "page-top"
    },
        html.div({"id": "wrapper"},
                 nabvar_side.navbar(),
                 html.div({"id": "content-wrapper", "class": "d-flex flex-column"},
                          html.div({"id": "content"},
                                   navbar_user.navbar_user(),
                                   html.div({"class": "container-fluid"},
                                            html.div({"class": "d-sm-flex align-items-center justify-content-between mb-4"},
                                                     html.h1(
                                                {"class": "h3 mb-0 text-gray-800"}, "Dashboard"),
                                       html.a({"class": "d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"},
                                              html.i(
                                           {"class": "fas fa-download fa-sm text-white-50 me-2"}),
                                                "Reporte de Ventas")
                                   ),
                              html.div({"class": "row d-flex"},
                                       card_icome.card_income(
                                  "primary", "Ingresos (Mensuales)", 40.000, "fas fa-calendar fa-2x text-gray-300"),
                                       card_icome.card_income(
                                  "success", "Ingresos (Anuales)", 215.000, "fas fa-dollar-sign fa-2x text-gray-300"),
                                       card_pending_request.card_pending_request(
                                  50),
                                       card_tasks.card_task(18)
                                   ),
                              html.div({"class": "row"},
                                       card_graphic_ventas.card_graphic_ventas(),
                                       card_graphic_round.card_grpahic_round()
                                       ),

                          ),
                 ),
            footer.footer()
        ), html.a({"class": "scroll-to-top rounded", "href": "#page-top"})
    ),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"})

    )
