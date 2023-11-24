from reactpy import component, html
from reactpy_router import link


@component
def shopping():

    return (
        html.div(

            html.div(
                link("Dashboard", to="/")
            ),
        )
    )
