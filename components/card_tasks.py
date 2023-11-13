from reactpy import component, html

#
@component
def card_task(request):

    return (
        html.div({"class": "col-xl-3 col-md-6 mb-4"},        
            html.div({"class":f'card border-left-warning shadow h-100 py-2'},
                html.div({"class":"card-body"},
                    html.div({"class":"row no-gutters align-items-center"},
                        html.div({"class":"col mr-2"},
                            html.div({"class":"text-xs font-weight-bold text-warning text-uppercase mb-1"},"ENVÍOS PENDIENTES"),
                            html.div({"class":"h5 mb-0 font-weight-bold text-gray-800"}, request)
                        ),
                        html.div({"class":"col-auto"},
                            html.i({"class":"fas fa-ship fa-2x text-gray-300"})
                        )
                    )
                )
            )
        ))