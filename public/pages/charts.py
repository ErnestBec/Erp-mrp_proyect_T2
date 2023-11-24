from reactpy import html, component
from components import nabvar_side, navbar_user, grafica_area, footer, grafica_barras, grafica_donas


@component
def graficas():

    return html.div(
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
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
        html.script(
            {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-bar-demo.js"})

    )
