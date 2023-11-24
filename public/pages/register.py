from reactpy import component, html
from reactpy_router import link


@component
def register():

    return (
        html.div(
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
        )
    )
