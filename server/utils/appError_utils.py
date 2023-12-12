from fastapi import Request, HTTPException
from starlette.responses import JSONResponse

# Esta funcion esta a la escucha de cualquier error que genere la aplicacion, ya sea a la hora de recibir datos esto nos permite regresarle al ususario mensaje de error personalizados segun sea el caso, esta funcion es asincrona ya que debe esperar a se termine la ejecucion de cada funcion para poder regresar un error en caso de que exista
async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# Esta funcion tambien captura los errores, pero son errores que no dependen de la API, como conexiona la base de datos
async def server_error_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )
