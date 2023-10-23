from reactpy import component, html
from components import nabvar_side, footer, navbar_user, card_icome , card_tasks, card_pending_request
from reactpy_router import link
from pages import home_page



@component
def utlities_oters():
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
                             html.h1({"class":"h3 mb-1 text-gray-800"},"Other Utilities"),
                             html.p({"class":"mb-4"},"Bootstrap's default utility classes can be found on the official"),
                             # Content Row
                             html.div({"class":"row"},
                                      html.div({"class":"col-lg-6"},
                                               #Overflow Hidden
                                               html.div({"class":"card mb-4"},
                                                        html.div({"class":"card-header py-3"},
                                                                 html.h6({ "class":"m-0 font-weight-bold text-primary"},"Overflow Hidden Utilty")
                                                                 ),
                                                        html.div({"class":"card-body"},"Use", html.code(".o-hidde")," to set the overflow property of any element to hidden.")
                                                        
                                                        
                                                        ),
                                                #Progress Small
                                                html.div({"class":"card mb-4"},
                                                         html.div({"class":"card-header py-3"},
                                                                  html.h6({"class":"m-0 font-weight-bold text-primary"},"Progress Small Utility")
                                                                    ),
                                                        html.div({"class":"card-body"},
                                                                 html.div({"class":"mb-1 small"},"Normal Progress Bar"),
                                                                 html.div({"class":"progress mb-4"},
                                                                          html.div({"class":"progress-bar", "role":"progressbar", "style":"width: 75%", "aria-valuenow":"75", "aria-valuemin":"0", "aria-valuemax":"100"})
                                                                           ),
                                                                html.div({"class":"mb-1 small"},"Small Progress Bar"),
                                                                html.div({"class":"progress progress-sm mb-2"},
                                                                         html.div({"class":"progress-bar", "role":"progressbar", "style":"width: 75%", "aria-valuenow":"75", "aria-valuemin":"0", "aria-valuemax":"100"})

                                                                         ),
                                                                "Use the <code>.progress-sm</code> class along with <code>.progress</code>"
                                                                
                                                                 
                                                                 
                                                                 )
 
                                                         ),
                                                #Dropdown No Arrow
                                                html.div({"class":"card mb-4"},
                                                         html.div({"class":"card-header py-3"},
                                                                  html.h6({ "class":"m-0 font-weight-bold text-primary"},"Dropdown - No Arrow")
                                                                  ),
                                                        html.div({"class":"card-body"},
                                                                 html.div({"class":"dropdown no-arrow mb-4"},
                                                                          html.button({"class":"btn btn-secondary dropdown-toggle", "type":"button", "id":"dropdownMenuButton", "data-toggle":"dropdown", "aria-haspopup":"true", "aria-expanded":"false"},
                                                                                      " Dropdown (no arrow)"
                                                                                      
                                                                                      ),
                                                                            html.div({"class":"dropdown-menu", "aria-labelledby":"dropdownMenuButton"},
                                                                                     html.a({"class":"dropdown-item", "href":"#"},"Action"),
                                                                                      html.a({"class":"dropdown-item", "href":"#"},"Another action"),
                                                                                       html.a({"class":"dropdown-item", "href":"#"},"Something else here"),
                                                                                     
                                                                                     )
                                                                          ),
                                                                          "Add the <code>.no-arrow</code> class alongside the <code>.dropdown</code>"
                                                                 
                                                                 )
                                                         )
                                               ),
                                        html.div({"class":"col-lg-6"},
                                                 #Roitation Utilities
                                                 html.div({"class":"card"},
                                                          html.div({"class":"card-header py-3"},
                                                                  html.h6({"class":"m-0 font-weight-bold text-primary"},"Rotation Utilities") 
                                                                   ),
                                                            html.div({"class":"card-body text-center"},
                                                                     html.div({"class":"bg-primary text-white p-3 rotate-15 d-inline-block my-4"},".rotate-15"),
                                                                     html.hr(),
                                                                     html.div({"class":"bg-primary text-white p-3 rotate-n-15 d-inline-block my-4"},".rotate-n-15")
                                                                     
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