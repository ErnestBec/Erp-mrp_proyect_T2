from reactpy import component, html

@component
def Tables():
    return html.table({"class":"table", "id":"table"},
        html.thead(
            html.tr(
                html.th(scope=""),
                html.th(scope="col", children="No"),
                html.th(scope="col", children="Codigo*"),
                html.th(scope="col", children="BOM No"),
                html.th(scope="col", children="Planned Qty*"),
                html.th(scope="col", children="Planned (Start Date) *"),
            )
        ),
        html.th(scope=""),
                html.th(scope="col", children="No"),
                html.th(scope="col", children="Codigo*"),
                html.th(scope="col", children="BOM No"),
                html.th(scope="col", children="Planned Qty*"),
                html.th(scope="col", children="Planned (Start Date) *"),
    )