from reactpy import component, html
from components import nabvar_side, footer, navbar_user, card_icome , card_tasks, card_pending_request
from reactpy_router import link
from pages import home_page



@component
def tablas():
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
        return html.div(
        bootstrap_css,
        style_css,
        fontawesome,
        head,
        html.div({
            "style": {
                "display": "flex",
            },
            "id":"page-top"
        },
            html.div(nabvar_side.navbar()),
            html.div({"style":{
                "width":"100%"
            }, "id":"content-wrapper", "class" :"d-flex flex-column"},
                html.div({"id":"content"},
                    html.div(navbar_user.navbar_user()),
                    html.div({"class":"container-fluid"},
                             #Page Heading
                             html.h1({"class":"h3 mb-2 text-gray-800"},"Tables"),
                             html.p({"class":"mb-4"},"DataTables is a third party plugin that is used to generate the demo table below."),
                             #Datables example
                             html.div({"class":"card sh adow mb-4"},
                                    html.div({"class":"card-header py-3"},
                                            html.h6({"class":"m-0 font-weight-bold text-primary"},"DataTables Examle")
                                            ),
                                    html.div({"class":"card-body"},
                                             html.div({"class":"table-responsive"},
                                                      html.table({"class":"table table-bordered", "id":"dataTable", "width":"100%", "cellspacing":"0"},
                                                                 html.thead(
                                                                         html.tr(
                                                                                 html.th("Name"),
                                                                                 html.th("EDAD"),
                                                                                 html.th("Office"),
                                                                                 html.th("Age"),
                                                                                 html.th("Start Date"),
                                                                                 html.th("Salary")
                                                                         )

                                                                 ),
                                                                 html.tfoot(
                                                                        html.tr(
                                                                                 html.th("Name"),
                                                                                 html.th("Position"),
                                                                                 html.th("Office"),
                                                                                 html.th("Age"),
                                                                                 html.th("Start Date"),
                                                                                 html.th("Salary")
                                                                         )       
                                                                 ),
                                                                 html.tbody(
                                                                         html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$326,800")
                                                                         ),
                                                                           html.tr(
                                                                                 html.td("Tiger Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("61"),
                                                                                 html.td("2011/04/25"),
                                                                                 html.td("$320,800")
                                                                         ),
                                                                          html.tr(
                                                                                 html.td("Emma Nixon"),
                                                                                 html.td("System Architec"),
                                                                                 html.td("Edinburgh"),
                                                                                 html.td("22"),
                                                                                 html.td("2011/04/25"),
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
        ),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery/jquery.min.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/bootstrap/js/bootstrap.bundle.min.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery-easing/jquery.easing.min.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/sb-admin-2.min.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/chart.js/Chart.min.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
        html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
        html.script({"src":"https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})
        
    )