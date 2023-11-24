from fastapi import Request, HTTPException


async def OrdenProd_validate_middleware(request: Request):
    errors = []
    orden = await request.json()
    if not orden["fecha_alta"]:
        errors.append("The fecha_alta cannot be empty")
    if not orden["solicitud"]:
        errors.append("The solicitud cannot be empty")
    if not orden["producto"]:
        errors.append("The producto cannot be empty")
    if not orden["cantidad_fabri"]:
        errors.append("The cantidad_fabri be empty")
    elif orden["cantidad_fabri"] < 0:
        errors.append("Te cantidad_fabri cannot be 0")
    if not orden["id_pieza"]:
        errors.append("The id_pieza cannot by empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))

 

async def OrdenProducc_update_validator(request: Request):
    errors = []
    orden = await request.json()
    if not orden["fecha_alta"]:
        errors.append("The fecha_alta cannot be empty")
    if not orden["solicitud"]:
        errors.append("The solicitud cannot be empty")
    if not orden["producto"]:
        errors.append("The producto cannot be empty")
    if not orden["cantidad_fabri"]:
        errors.append("The cantidad_fabri be empty")
    elif orden["cantidad_fabri"] < 0:
        errors.append("Te cantidad_fabri cannot be 0")
    if not orden["id_pieza"]:
        errors.append("The id_pieza cannot by empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))