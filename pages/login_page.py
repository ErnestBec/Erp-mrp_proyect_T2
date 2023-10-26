from reactpy import component, html
from reactpy_router import link


@component
def login_user():
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

    ),

    return (
        html.div({"class": "bg-gradient-primary", "style": {"height": "100vh"}},
                 bootstrap_css,
                 style_css,
                 fontawesome,
                 head,
                 html.div({"class": "container"},
                          html.div({"class": "row justify-content-center"},
                                   html.div({"class": "col-xl-10 col-lg-12 col-md-9"},
                                            html.div({"class": "card o-hidden border-0 shadow-lg my-5"},
                                                     html.div({"class": "card-body p-0"},
                                                              html.div({"class": "row"},
                                                                       html.div(
                                                                           {"class": "col-lg-6 d-none d-lg-block bg-login-image"},),
                                                                       html.div({"class": "col-lg-6"},
                                                                                html.div({"class": "p-5"},
                                                                                         html.div({"class": "text-center"},
                                                                                                  html.h1(
                                                                                                      {"class": "h4 text-gray-900 mb-4"}, "Welcome Back!"),
                                                                                                  ),
                                                                                         html.form({"class": "user"},
                                                                                                   html.div({"class": "form-group"},
                                                                                                            html.input({"type": "email", "class": "form-control form-control-user", "id": "exampleInputEmail",
                                                                                                                        "aria-describedby": "emailHelp",
                                                                                                                        "placeholder": "Enter Email Address..."
                                                                                                                        })
                                                                                                            ),
                                                                                         html.div({"class": "from-group"},
                                                                                                  html.input({"type": "password", "class": "form-control form-control-user",
                                                                                                              "id": "exampleInputPassword", "placeholder": "Password"
                                                                                                              })
                                                                                                  ),
                                                                                         html.div({"class": "form-group"},
                                                                                                  html.div({"class": "custom-control custom-checkbox small"},
                                                                                                           html.input(
                                                                                                               {"type": "checkbox", "class": "custom-control-input", "id": "customCheck"}),
                                                                                                           html.label(
                                                                                                               {"class": "custom-control-label", "for": "customCheck"}, "Remember Me")
                                                                                                           ),
                                                                                                  ),
                                                                                         link(
                                                                                             "Login", to="/", **{"class": "btn btn-primary btn-user btn-block"}),
                                                                                         html.hr(),
                                                                                         html.a({"href": "index.html", "class": "btn btn-google btn-user btn-block"},
                                                                                                html.i(
                                                                                             {"class": "fab fa-google fa-fw"}),
                                                                                             "Login with Google"
                                                                                         ),
                                                                                         html.a({"href": "index.html", "class": "btn btn-facebook btn-user btn-block"},
                                                                                                html.i(
                                                                                             {"class": "fab fa-facebook-f fa-fw"}),
                                                                                             "Login with Facebook"
                                                                                         )
                                                                                         ),
                                                                                         html.hr(),
                                                                                         html.div({"class": "text-center"},
                                                                                                  html.a(
                                                                                             {"class": "small", "href": "#"}, "Forgot Password?")
                                                                                ),
                                                                           html.div({"class": "text-center"},
                                                                                    link("Create an Account!", to="/register",
                                                                                         **{"class": "small", "href": "#"})
                                                                                    )
                                                                       )
                                                              )
                                                     )
                                            )
                                   )
                          )
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
