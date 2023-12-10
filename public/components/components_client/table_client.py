from reactpy import component, html
# Compenente que genera los headers de la tabla
@component
def list_headers(headers):
    list_th = [html.th(head) for head in headers]
    return html.tr(list_th)

# Componente que genera la el cuerpo de la tabla
@component
def list_data (content):
    list_td =[]
    list_tr=[]
    for data  in content:
        td_data =[]
        for td in data:
            if td == "pending":
                td_data.append(html.td(html.span({"class_name":"rounded-3 p-1 ","style":{"background-color":"#f5e679"}},"Pendiente")))
            elif td == "complete":
                td_data.append(html.td(html.span({"class_name":"rounded-3 p-1 ","style":{"background-color":"#8fd6e7"}},"Completado")))
            elif td == "paid":
                td_data.append(html.td(html.span({"class_name":"rounded-3 p-1 ","style":{"background-color":"#9afc86"}},"Pagado")))
            else:
                td_data.append(html.td({"class_name":"text-dark"},td))
        list_td.append(td_data)
    
    for tr in list_td:
        list_tr.append(html.tr(tr))        
    return html.tbody(list_tr)
 
# Componente que es toda la tabla de los datos ingresados
@component
def TableClient(headers, content):
    return html.table({"class_name":"table  table-hover"},
                      html.thead(
                         list_headers(headers)
                      ),
                        list_data(content)
                      )