from reactpy import component, html
from reactpy_router import link



@component
def linearChartComponent(canvaId:str,titles_x:str,title:str,charts:str):
    script =html.script("const ctx = document.getElementById('"+canvaId+"'); new Chart(ctx, { type: 'line', data: { labels: "+titles_x+", datasets: "+charts+"}});")
    return (
        html.div({"class": "col-xl-8 col-lg-7"},
            html.div({"class": "card shadow mb-4"},
                     html.div({"class": "card-header py-3 d-flex flex-row align-items-center justify-content-between"},
                              html.h6({"class": "m-0 font-weight-bold text-primary"}, title),
                    ),
                    html.div({"class": "card-body"},
                         html.div({"class": "chart-area"},
                                  html.canvas(
                                  {"id": canvaId})
                        )
                    )
            ),
            script
        )
    )
