from reactpy import html, component


@component
def Tabla(columnas, documentos):
    def generar_filas_tabla(documentos):
        filas_tabla = []
        for i, doc in enumerate(documentos):
            fila = [
                html.th({"scope": "row"}, str(i + 1)),
                *[html.td(obtener_valor(doc, columna)) for columna in columnas[1:]],
            ]
            filas_tabla.append(html.tr(*fila))
        return filas_tabla

    def obtener_valor(doc, columna):
        if "." in columna:
            atributos = columna.split(".")
            valor = doc
            for atributo in atributos:
                if isinstance(valor, dict) and atributo in valor:
                    valor = valor[atributo]
                elif isinstance(valor, list) and atributo.isdigit():
                    indice = int(atributo)
                    if indice < len(valor):
                        valor = obtener_valor(valor[indice], ".".join(atributos[2:]))
                    else:
                        valor = ""
                    break
                else:
                    valor = ""
                    break
        else:
            valor = doc.get(columna, "")
        return valor

    filas_tabla = generar_filas_tabla(documentos)

    tabla = html.table(
        {"class": "table", "id": "dataTable"},
        html.thead(
            {"style": "text-align: center;"},
            html.tr(*[html.th({"scope": ""}, encabezado) for encabezado in columnas]),
        ),
        html.tbody({"style": "text-align: center;"}, *filas_tabla),
    )

    contenedor_tabla = html.div(
        {"class": "table-responsive", "style": "margin-top: 2%;"}, tabla
    )
    return contenedor_tabla
