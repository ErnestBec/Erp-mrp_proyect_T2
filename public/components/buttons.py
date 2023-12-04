from reactpy import component, html

@component
def ButtonEstatus(estado):
    color, background_color = '', ''

    if estado == 'aceptado':
        color = '#000000'
        background_color = '#D0F4FF'
    elif estado == 'pendiente':
        color = '#000000'
        background_color = '#FBF5C4'
    else:
        color = '#000000'
        background_color = '#FFDFDF'

    return html.button(
        type="button",
        className="btn",
        style={"color": color, "background-color": background_color},
        children=html.b(estado),
    )
