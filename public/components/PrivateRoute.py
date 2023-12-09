from reactpy import component, Redirect

def PrivateRoute(props):
    # Obtener el estado de autenticación
    # (Por ejemplo, usando useReducer o cualquier otro método de manejo del estado)
    
    # Si el usuario está autenticado, renderizar el componente
    if is_authenticated:
        return component(props.component, props.props)
    # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
    else:
        return Redirect({'to': '/login'})