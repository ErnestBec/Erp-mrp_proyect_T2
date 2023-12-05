from reactpy import component, html

@component
def Tabla(columnas, datos):
   
    table_rows = [
        html.tr(
            html.th({"scope": "row"}, str(i + 1)),
            *[html.td(data) for data in variable]
        ) for i, variable in enumerate(datos)
    ]

    table = html.table(
        {"class": "table", "id": "dataTable"},
        html.thead(
            {"style": "text-align: center;"},
            html.tr(
                *[html.th({"scope": ""}, header) for header in columnas]
            )
        ),
        html.tbody(
            {"style": "text-align: center;"},
            *table_rows
        )
    )

    table_container = html.div(
        {"class": "table-responsive", "style": "margin-top: 2%;"},
        table
    )
    return table_container










