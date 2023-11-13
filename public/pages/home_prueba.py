from reactpy import component , html, hooks

#
@component
def home_peueba():
    color, setColor= hooks.use_state("bg-primary")

    return html.div({"class":"container-fluid"},
         html.div({"class": f'{color}', "style":{"width":"230px"}},"Hola x2" ),
         html.button({"class":"btn-primary", "on_click": lambda event:setColor("bg-dark")},'hola perros'),
     html.button({"class":"btn-primary", "on_click": lambda event:setColor("bg-primary")},'hola perros regresa')
                   
                    
                    
    )
