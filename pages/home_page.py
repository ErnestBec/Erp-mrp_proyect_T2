from reactpy import html, component
from components import nabvar_side, navbar_user, card_icome, card_tasks, card_pending_request, footer, card_graphic_ventas, card_graphic_round
from components import chart

@component
def home_page():
    chartTitle1 = "Some title"
    titles = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr',  'May', 'Jun'] 
    charts = [chart.newChart("silk",[15, 70, 55, 250, 320, 260, 250, 100, 150, 200, 300],"#F98600"),chart.newChart("cotton",[30, 250, 240, 200, 200, 430, 430, 500, 650, 390, 270, 850],"#00BA34")]
    strCharts = "["
    for i in charts:
        strCharts+=(i+",")
    strCharts+="]"
    
    return html.div({"id": "page-top"},
                    html.div({"id": "wrapper"},
                             html.div({"id": "content-wrapper", "class": "d-flex flex-column"},
                                      html.div({"id": "content"},
                                               html.div({"class": "container-fluid"},
                                                        html.div({"class": "row"},
                                                                 card_graphic_ventas.LinearChartComponent("myChart1",str(titles),chartTitle1,strCharts)
                                                        )
                                                )
                                    )
                            )
                    )
    )
