from reactpy import html, component
from components import nabvar_side, navbar_user, grafica_area, footer, grafica_barras, grafica_donas

#
@component
def graficas():
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
        html.title("Gráficas"),
        html.link({
            "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
            "rel": "stylesheet"
        }),

    ),
    return html.div(
        bootstrap_css,
        style_css,
        fontawesome,
        head,
        html.div({
            "style": {
                "display": "flex",
            },
            "id": "page-top"
        },
            nabvar_side.navbar(),
            html.div({"style": {
                "width": "100%"
            }, "id": "content-wrapper", "class": "d-flex flex-column"},
                html.div({"id": "content"},
                         html.div(navbar_user.navbar_user()),
                         html.div({"class": "container-fluid"},
                                  html.div({"class": "d-sm-flex align-items-center justify-content-between mb-4"},
                                           html.h1(
                                      {"class": "h3 mb-0 text-gray-800"}, "Gráficas")
                         ),
                    html.div({"class": "row d-flex"},
                             grafica_area.grafica_area(
                        "myAreaChart", "45px", "160px"),
                             grafica_barras.grafica_barras(
                        "myAreaChart", "45px", "160px"),
                             grafica_donas.grafica_donas(
                        "myAreaChart", "45px", "160px")

                         )
                    # html.div(componentes.login_user())
                ),
                html.div()
            ),
                footer.footer()

        )
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
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-bar-demo.js"}),
        html.script(
            {"src": "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})

    )
