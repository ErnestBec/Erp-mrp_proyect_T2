from reactpy import component, html
from reactpy_router import link
from components import card_graphic_ventas
@component
def Dashboard():
    return html.div(
        card_graphic_ventas.linearChartComponent()
    )