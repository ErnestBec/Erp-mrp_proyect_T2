from reactpy import component, html
from components import nabvar_side, footer, navbar_user, card_icome, card_tasks, card_pending_request
from reactpy_router import link
from pages import home_page


@component
def tablas():

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
                              # Page Heading
                              html.h1(
                                  {"class": "h3 mb-2 text-gray-800"}, "Tables"),
                              html.p(
                                  {"class": "mb-4"}, "DataTables is a third party plugin that is used to generate the demo table below."),
                              # Datables example
                              html.div({"class": "card sh adow mb-4"},
                                       html.div({"class": "card-header py-3"},
                                                html.h6(
                                           {"class": "m-0 font-weight-bold text-primary"}, "DataTables Examle")
                              ),
                         html.div({"class": "card-body"},
                                  html.div({"class": "table-responsive"},
                                           html.table({"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0"},
                                                      html.thead(
                                               html.tr(
                                                   html.th(
                                                       "Name"),
                                                   html.th(
                                                       "EDAD"),
                                                   html.th(
                                                       "Office"),
                                                   html.th(
                                                       "Age"),
                                                   html.th(
                                                       "Start Date"),
                                                   html.th(
                                                       "Salary")
                                               )

                                           ),
                                      html.tfoot(
                                               html.tr(
                                                   html.th("Name"),
                                                   html.th(
                                                       "Position"),
                                                   html.th("Office"),
                                                   html.th("Age"),
                                                   html.th(
                                                       "Start Date"),
                                                   html.th("Salary")
                                               )
                                           ),
                                      html.tbody(
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Tiger Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("61"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$320,800")
                                               ),
                                               html.tr(
                                                   html.td(
                                                       "Emma Nixon"),
                                                   html.td(
                                                       "System Architec"),
                                                   html.td(
                                                       "Edinburgh"),
                                                   html.td("22"),
                                                   html.td(
                                                       "2011/04/25"),
                                                   html.td("$326,800")
                                               )

                                           )



                                  )

                         )

                              )



                     )

            )


            ),

            footer.footer()

        )
        )
    )
