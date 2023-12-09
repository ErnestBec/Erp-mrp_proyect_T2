from reactpy import component, html, hooks,use_state,create_context
from reactpy_router import link
import reactpy
import json
import requests
#
url = "http://tier2-pe.eastus.cloudapp.azure.com:8001/"
def btnSubmit(e,mail,pswd):
    info = {"email": str(mail),"password": str(pswd)}
    color ="#ff6161"
    result = ""
    link = ""
    response = requests.post(url+"login",data=json.dumps(info))
    if response.status_code >=200 and response.status_code <300:
        color = "#98ff98"
        result = str(response.json()['token'])
        res = "localStorage.clear();localStorage.setItem(\"token\", \""+result+"\");window.location.href = \"/dashboard\";"
        return html.script(res)
    else:
        return html.script("localStorage.clear();")
    
    
@component
def login_user():
    
    email,setEmail = reactpy.hooks.use_state("")
    passwd,setPasswd=reactpy.hooks.use_state("")
    msj, setMsj = reactpy.hooks.use_state("")
    return (
        html.div({"style":"background-color: #FAFCFD;height: 100vh;","class":"d-flex align-items-center"},
                 html.head(html.title('Login')),
                 html.div({"class": "container-fluid h-75"},
                          html.div({"class":"row d-flex justify-content-center h-100"},
                                   html.div({"style":"padding: 0px; border-radius: 24px;background-color: #FFFFFF;box-shadow: 1px 0px 12px 0px rgba(0,0,0,0.04);","class":"col-10 col-md-6 col-lg-5 col-xl-3 h-100"},
                                            html.div({"style":"border-radius: 24px;","class":"container-fluid h-100"},
                                                     html.div({"class":"row h-75","style":"background-color: white;border-top-right-radius: 24px;border-top-left-radius: 24px;"},
                                                              html.div({"class":"col-12 pb-1 pt-3 pe-0 ps-0 pb-sm-2 pt-sm-4 pe-sm-2 ps-sm-2 pb-lg-3 pt-lg-5 pe-lg-4 ps-lg-4"},
                                                                       html.div({"class": "h-100"},
                                                                                html.div({"class":"w-100","style":"color: #47516B; font-size: 24px; font-family: Inter; font-weight: 800; line-height: 32px; word-wrap: break-word"},
                                                                                         "Inicia sesión."
                                                                                         ),
                                                                                html.div({"class":"w-100 mb-4","style":"opacity: 0.60; color: #47516B; font-size: 20px; font-family: Inter; font-weight: 400; line-height: 28px; word-wrap: break-word"},
                                                                                         "Accede con tus credenciales."
                                                                                         ),
                                                                                html.form({}, 
                                                                                          html.div({"class":"form-group"},
                                                                                                   html.label({"for":"exampleInputEmail1","style": "color: #556769; font-size: 12px; font-family: Inter; font-weight: 500; line-height: 16px; word-wrap: break-word"},"Correo electrónico*"),
                                                                                                   html.input({"type":"email","class":"form-control","id":"exampleInputEmail1","aria-describedby":"emailHelp","placeholder":"correo@example.com","key":"mail1","onChange":lambda event:setEmail(str(event['currentTarget']['value']))})
                                                                                                   ),
                                                                                          html.div({"class":"form-group"},
                                                                                                   html.label({"for":"exampleInputPassword1","style": "color: #556769; font-size: 12px; font-family: Inter; font-weight: 500; line-height: 16px; word-wrap: break-word"},"Contraseña"),
                                                                                                   html.input({"type":"password","class":"form-control mb-4","id":"exampleInputPassword1","placeholder":"Ingresa contraseña","onChange":lambda event:setPasswd(str(event['currentTarget']['value']))})
                                                                                                   ),
                                                                                          msj,
                                                                                          html.button({"type":"button","class":"btn btn-dark col-12","onClick":lambda event:setMsj(btnSubmit(event,email,passwd))},"Iniciar Sesión")
                                                                                          )
                                                                                )
                                                                       )
                                                              ),
                                                     html.div({"class": "row h-25 ps-5 pe-5 pt-4 pb-4 flex-column justify-content-start align-items-start gap-2","style":"background-color: #E8E8E8;border-bottom-right-radius: 24px;border-bottom-left-radius: 24px;"},
                                                              html.div({"style":"opacity: 0.70; color: #4D70A4; font-size: 12px; font-family: Inter; font-weight: 400; line-height: 16px; word-wrap: break-word"},
                                                                       "©2023 ElectroniXpress. Todos los derechos reservados."
                                                                       ),
                                                              html.div({"style":"color: #181616; font-size: 12px; font-family: Inter; font-weight: 700; line-height: 16px; word-wrap: break-word"},
                                                                       "Política de Privacidad.")
                                                              )
                                                     )
                                            )
                                   )
                          )
                 )
    )
