from reactpy import component, html
from reactpy_router import link





@component
def error():
   
    return (
            html.div( {"id":"page-top","style":{"height":"100vh"},"class_name":"d-flex align-items-center"},
                    html.div({"class":"container-fluid"},
                                                html.div({"class":"text-center"},
                                                     html.div({ "class":"error mx-auto", "data-text":"404"},"404"),
                                                     html.p({"class":"lead text-gray-800 mb-5"},"Page Not Found"),
                                                     html.p({"class":"text-gray-500 mb-0"},"It looks like you found a glitch in the matrix.."),
                                                     html.a(link("Regresar al inicio",to="/User_Dashboard",**{"class":"text-gray-500 mb-0"}))
                                                     )),
                    )


        
    )