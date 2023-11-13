from reactpy import component, html

#
@component
def card_income(colo_rborder,income, cash, icon):

    return (
        html.div({"class": "col-xl-3 col-md-6 mb-4"},        
            html.div({"class":f'card border-left-{colo_rborder} shadow h-100 py-2'},
                html.div({"class":"card-body"},
                    html.div({"class":"row no-gutters align-items-center"},
                        html.div({"class":"col mr-2"},
                            html.div({"class":f'text-xs font-weight-bold text-{colo_rborder} text-uppercase mb-1'},income),
                            html.div({"class":"h5 mb-0 font-weight-bold text-gray-800"}, f'${cash}')
                        ),
                        html.div({"class":"col-auto"},
                            html.i({"class":f'{icon}'})
                        )
                    )
                )
            )
        ))
