from reactpy import component, html
#
@component
def footer():
    
   return( 
        html.footer({"class":"sticky-footer bg-white"},
                    html.div({"class":"container my-auto"},
                        html.div({"class":"copyright text-center my-auto"},
                            html.span("Copyright",html.i({"class":"far fa-copyright"}),  "Your Website 2021")
                        )         
                    )
        )       
    )