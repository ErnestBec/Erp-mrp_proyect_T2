from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer, card_graphic_ventas, card_graphic_round
from components import chart as classChart
import random

@component
def home_page():
    return html.div({"id": "page-top"},
                    html.div({"id": "wrapper"},
                             html.div({"id": "content-wrapper", "class": "d-flex flex-column"},
                                      html.div({"id": "content"},
                                               html.div({"class": "container-fluid"},
                                                        html.div({"class": "row"},
                                                                 makeAChart("mychar1"),
                                                                 makeAChart("mychar2")
                                                        )
                                                )
                                    )
                            )
                    )
    )
def makeAChart(nombre_char:str):
    chartTitle1 = "Some title"
    titles = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr',  'May', 'Jun'] 
    charts = []
    arrayTemp =[]
    palabras_adj = ["Rojo", "Azul", "Verde", "Brillante", "Suave", "Rápido", "Silencioso", "Elegante"]
    palabras_sust = ["León", "Montaña", "Río", "Estrella", "Cascada", "Árbol", "Globo", "Martillo"]
    for i in range(random.randint(1, 7)):
        adjetivo = random.choice(palabras_adj)
        sustantivo = random.choice(palabras_sust)
        nombre_aleatorio = f"{sustantivo} {adjetivo}"
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
        arrayTemp.clear()
        for i in range(11):
            arrayTemp.append(random.randint(1, 550))
        charts.append(classChart.newChart(str(nombre_aleatorio),arrayTemp,str(color_hex)))
        strCharts = "["
    for i in charts:
        strCharts+=(i+",")
    strCharts+="]"
    return card_graphic_ventas.LinearChartComponent(nombre_char,str(titles),chartTitle1,strCharts)