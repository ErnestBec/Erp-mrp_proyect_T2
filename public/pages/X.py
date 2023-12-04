
from reactpy import component, html, useState

@component
def App():
    # Definir los datos y las columnas
    datos = [
        ["Aieto Energies", "Aprobada", "0957746KJLY", "BOM-Rizz-0523-001", "24/12/2020"],
        ["Aieto Energies", "Pendiente", "0957746KJLY", "BOM-Rizz-0523-001", "24/12/2020"],
        ["Aieto Energies", "Completada", "0957746KJLY", "BOM-Rizz-0523-001", "24/12/2020"],
        ["Aieto Energies", "No Empezada", "0957746KJLY", "BOM-Rizz-0523-001", "24/12/2020"],
    ]

    columnas = ["", "Nombre del Cliente", "Estado", "ID de la Orden", "Lista de Materiales", "Fecha de Vencimiento"]

    # Definir las opciones del dropdown
    opciones = ["Ordenes Totales", "Ordenes Pendientes", "Ordenes Aprobadas", "Ordenes Completadas"]

    # Estado para almacenar la opción seleccionada
    opcion_seleccionada, setOpcionSeleccionada = useState(opciones[0])

    # Filtrar los datos según la opción seleccionada
    datos_filtrados = [dato for dato in datos if opcion_seleccionada in dato]

    # Renderizar la aplicación
    return html.div(
        btnFilter(opciones, setOpcionSeleccionada),
        Tabla(columnas, datos_filtrados)
    )

@component
def btnFilter(opciones, setOpcionSeleccionada):
    dropdown_options = [
        html.li(html.a({"class": "dropdown-item", "href": "#", "onClick": lambda _: setOpcionSeleccionada(option)}, option)) for option in opciones
    ]

    return html.div(
        {"class": "dropdown ms-2"},
        html.button(
            {
                "class": "btn btn-light dropdown-toggle",
                "type": "button",
                "style": "color: #000000;",
                "data-bs-toggle": "dropdown",
                "aria-expanded": "false",
            },
            html.b("Filtrar por"),
        ),
        html.ul({"class": "dropdown-menu"}, *dropdown_options),
    )

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

# Lanzar la aplicación
if __name__ == "__main__":
    App.run()