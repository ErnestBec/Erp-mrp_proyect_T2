from reactpy import html, component

@component
def Table():
    return html.table(
        {"className": "table", "id": "dataTable"},
        html.thead(
            html.tr(
                html.th(scope=""),
                html.th(scope="col", children="No"),
                html.th(scope="col", children="Codigo*"),
                html.th(scope="col", children="BOM No"),
                html.th(scope="col", children="Planned Qty*"),
                html.th(scope="col", children="Planned (Start Date) *"),
            ),
        ),
        html.tbody(
            html.tr(
                html.th(scope="row", children="1"),
                html.td(children="Mark"),
                html.td(children="Otto"),
                html.td(children="$300.00USD"),
                html.td(children=""),
                html.td(children="20/11/2023"),
            ),
            html.tr(
                html.th(scope="row", children="2"),
                html.td(children="Jacob"),
                html.td(children="Thornton"),
                html.td(children="$100.00USD"),
                html.td(children="Holi"),
                html.td(children="20/11/2023"),
            ),
            html.tr(
                html.th(scope="row", children="3"),
                html.td(children="Larry the Bird"),
                html.td(children="@twitter"),
                html.td(children="$200.00USD"),
                html.td(children=""),
                html.td(children="20/11/2023"),
            ),
        ),
    )
