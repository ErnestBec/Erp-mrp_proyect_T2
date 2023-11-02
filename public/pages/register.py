from reactpy import component, html
from reactpy_router import link


@component
def register():
    bootstrap_css = html.link({
        "rel": "stylesheet",
        "href": "https://elpatronhh.github.io/portfolio/bootstrap.min.css"
    }),
    style_css = html.link({
        "href": "https://elpatronhh.github.io/portfolio/sb-admin-2.min.css",
        "rel": "stylesheet"
    }),
    fontawesome = html.link({
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
    }),
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
        html.title("Registrar"),
        html.link({
            "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
            "rel": "stylesheet"
        }),

    ),

    return (
        html.div(
            bootstrap_css,
            style_css,
            fontawesome,
            head,
            html.div({"class": "bg-gradient-primary d-flex align-items-center", "style": {"height": "100vh"}},
                     html.div({"class": "container"},
                     html.div({"class": "row justify-content-center"},
                              html.div({"class": "card o-hidden border-0 shadow-lg "},
                                       html.div({"class": "card-body p-0"},
                                                html.div({"class": "row"},
                                                         html.div(
                                                    {"class": "col-lg-5 d-none d-lg-block bg-register-image"},),
                                           html.div({"class": "col-lg-7"},
                                                    html.div({"class": "p-5"},

                                                    html.div({"class": "text-center"},
                                                             html.h1(
                                                        {"class": "h4 text-gray-900 mb-4"}, "Crear cuenta")
                                                    ),
                                               html.form({"class": "user"},
                                                         html.div({"class": "form-group row"},
                                                                  html.div({"class": "col-sm-6 mb-3 mb-sm-0"},
                                                                           html.input(
                                                                           {"class": "form-control form-control-user", "type": "text", "placeholder": "Nombre"})
                                                                           ),
                                                                  html.div({"class": "col-sm-6"},
                                                                           html.input(
                                                                      {"class": "form-control form-control-user", "type": "text", "placeholder": "Apellido"})
                                                         )
                                               ),
                                                   html.div({"class": "form-group"},
                                                            html.input(
                                                            {"class": "form-control form-control-user", "type": "email", "placeholder": "Nombre"})
                                                            ),
                                                   html.div({"class": "form-group row"},
                                                            html.div({"class": "col-sm-6 mb-3 mb-sm-0"},
                                                                     html.input(
                                                                {"class": "form-control form-control-user", "type": "password", "placeholder": "Contraseña"})
                                                   ),
                                                   html.div({"class": "col-sm-6"},
                                                            html.input(
                                                            {"class": "form-control form-control-user", "type": "password", "placeholder": "Repite contraseña"})
                                                            )
                                               ),
                                                   link("Registrarse", to="/login", **{
                                                       "class": "btn btn-primary btn-user btn-block"
                                                   })
                                                    ),
                                               html.hr(),
                                               html.div({"class": "text-center"},
                                                        html.a(
                                                   {"class": "small", "href": "forgot"}, "¿Olvidaste tu contraseña?")
                                                    )
                                           )

                                                )))))
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
                {"src": "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})
        )
    )
