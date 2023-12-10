from reactpy import component, use_router

def Redirect(props):
    router = use_router()
    router.push(props.to)
    return component('span', {'style': {'display': 'none'}})