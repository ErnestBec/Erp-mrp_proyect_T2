# Este  es el middleware de autenticacion, es el encargado de validar token, validar el tipo de usuario que esta logeado y de esta manera permitirle o no el acceso a ciertas rutas 

from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from starlette.requests import Request
from utils.db import db_name

# indica los dias que estara activo el token, recibe como parametro el numero de dias que estara vigente el token de sesion
def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

# Funcion que recibe los datos el usuario para generar el token con sus credenciales  que recibe como poarametro, retorna el token ya generado
def write_token(data: dict):
    # Genera el token con los datos del ususario registrado, con los dias de expiracion y el metodo con que se cifrara el token
    token = encode(payload={**data, "exp": expire_date(2)},
                   key=getenv("SECRET"), algorithm="HS256")
    return token

# Esta funcion valida si el token es valido es decir si cumple con el metodo de cifrado, ademas de Verifica si el token esta activo o cumplio con el tiempo de expiracion definido,  en caso de no serlo retorna un mensaje de error segun sea el caso, recibe el token y retorna el token en caso de cumplir con las especificaciones 
def validate_token(token: str) -> dict:
    try:
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    return token

# Esta funcion es quien regresa los datos del usuario logueado como su correo ademas que este middleware nos sirve para vlidar que exista un usuario registrado, aqui mandamos a llamar la funcion que valida el token
class Portador(HTTPBearer):
    async def __call__(self, request: Request):
        authorization = await super().__call__(request)
        validate_token(authorization.credentials)
        token = authorization.credentials
        token_data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        return token_data

# Esta funcion nos ayuda a validar el rol del usuario o que el token pertenezcan a un usuario registrado en nuestra bd, em caso de no ser admin no permitira el acceso al endpoint
class protectedAcountAdmin(HTTPBearer):
    async def __call__(self, request: Request):
        authorization = await super().__call__(request)
        # del token recibido obtenemos sus credenciales
        token = authorization.credentials
        # Desencriptamos el token para verificar si es del tipo hs256
        token_data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        # buscamos las credenciales en la bd 
        user = db_name.Users.find_one(
            {"$and": [{"email": token_data["email"]}, {"status": "activate"}]})
        if not user:
            raise HTTPException(status_code=400, detail="user not account")
        if user["role"] == "client":
            raise HTTPException(status_code=400, detail="Access denied!")
        return user
