from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer, card_graphic_ventas, card_graphic_round

#
@component
def home_page():
    
    bootstrap_css = html.link({
        "rel": "stylesheet",
        "href": "https://elpatronhh.github.io/portfolio/bootstrap.min.css"
    })
    style_css = html.link({
        "href": "https://elpatronhh.github.io/portfolio/sb-admin-2.min.css",
        "rel": "stylesheet"
    })
    fontawesome = html.link({
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
    })
    head = html.div(
        html.meta({
            "charset": "utf-8"
        }),
        html.meta({
            "http-equiv": "X-UA-Compatible",
            "content": "IE=edge"
        }),
        html.meta({
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
        }),
        html.meta({
            "name": "description",
            "content": ""
        }),
        html.meta({
            "name": "author",
            "content": ""
        }),
        html.title("PANEL ADMINISTRADOR"),
        html.link({
            "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
            "rel": "stylesheet"
        }),
    )
    return html.div({
        "id": "page-top"
    },
        bootstrap_css,
        style_css,
        fontawesome,
        head,

        html.div({"id": "wrapper"},
                 nabvar_side.navbar(),
                 html.div({"id": "content-wrapper", "class": "d-flex flex-column"},
                          html.div({"id": "content"},
                                   html.div(navbar_user.navbar_user()),
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
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery/jquery.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/bootstrap/js/bootstrap.bundle.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery-easing/jquery.easing.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/sb-admin-2.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/chart.js/Chart.min.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
        html.script(
            {"src": "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})

    )
