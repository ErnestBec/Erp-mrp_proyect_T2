from reactpy import component, html


@component
def grafica_donas(id,width,heigth):

    return (
         html.div({"class":"card shadow mb-4"},
        html.div({"class":"card-header py-3"},html.h6({"class":"m-0 font-weight-bold text-primary"},"Gráfica de dona")),
        html.div({"class":"card-body"},
        html.div({"class":"chart-pie pt-4"},
        html.div({"class":"chartjs-size-monitor"},
                html.div({"class":"chartjs-size-monitor-expand"},
                html.div()
                ) ,             
                html.div({"class":"chartjs-size-monitor-shrink"},
                html.div()
                )       
        ),
        html.canvas({"id":"myPieChart","style":f"display : block; width : {width}; heigth : {heigth};","width":f"{width}","heigth":f"{heigth}", "class":"chartjs-render-monitor"})
        ))))
