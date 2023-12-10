from reactpy import component, html


from reactpy import hooks
@component
def btnFilterDay(request_data_month):
    def handle_change(event):
       request_data_month(event["target"]["value"])
    return html.select({"class_name":"form-select", "aria-label":"Default select example","onChange": handle_change},
                       html.option({"value":"13"},"Ver todas"),
                       html.option({"value":"01"},"Enero"),
                       html.option({"value":"02"},"Febrero"),
                       html.option({"value":"03"},"Marzo"),
                       html.option({"value":"04"},"Abril"),
                       html.option({"value":"05"},"Mayo"),
                       html.option({"value":"06"},"Junio"),
                       html.option({"value":"07"},"Julio"),
                       html.option({"value":"08"},"Agosto"),
                       html.option({"value":"09"},"Septiembre"),
                       html.option({"value":"10"},"Octubre"),
                       html.option({"value":"11"},"Noviembre"),
                       html.option({"value":"12"},"Diciembre"),
              
                       )
