from reactpy import component, html

@component
def btnFilter(opciones,request_data_status):
    select_options = []
    for option in opciones:
        select_options.append(html.option({"value":option},option))
    def handle_change(event):
       request_data_status(event["target"]["value"])
    return html.select({"class_name":"form-select ms-2", "aria-label":"Default select example","onChange":handle_change},                  
                       *select_options,
    )


