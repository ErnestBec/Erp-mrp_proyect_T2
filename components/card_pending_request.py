from reactpy import component, html

#
@component
def card_pending_request(percentage):

    return (
        html.div({"class": "col-xl-3 col-md-6 mb-4"},        
            html.div({"class":f'card border-left-info shadow h-100 py-2'},
                html.div({"class":"card-body"},
                    html.div({"class":"row no-gutters align-items-center"},
                        html.div({"class":"col mr-2"},
                            html.div({"class":f'text-xs font-weight-bold text-info text-uppercase mb-1'},"Almacen"),
                            html.div({"class":"h5 mb-0 font-weight-bold text-gray-800"}, f'%{percentage}')
                        ),
                        html.div({"class":"col"},
                            html.div({"class":"progress progress-sm mr-2"},
                                html.div({"class":"progress-bar bg-info",
                                        "role":"progressbar",
                                        "style":f'width: {percentage}%', "aria-valuenow":"50", "aria-valuemin":"0",
                                        "aria-valuemax":"100"
                                    }
                                )
                            )
                        ),
                        html.div({"class":"col-auto"},
                            html.i({"class":"fas fa-clipboard-list fa-2x text-gray-300"})
                        )
                    )
                )
            )
        ))