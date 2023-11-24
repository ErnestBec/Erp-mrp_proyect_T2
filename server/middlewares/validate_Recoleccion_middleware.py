from fastapi import Request, HTTPException


async def recoleccion_validate_middleware(request: Request):
    errors = []
    recoleccion = await request.json()
    if not recoleccion["fecha"]:
        errors.append("The fech cannot be empty")
    if not recoleccion["lugar"]:
        errors.append("The lugar cannot be empty")
    if not recoleccion["id_cobro"]:
        errors.append("The id_cobro cannot be empty")
    if not recoleccion["cobro"]:
        errors.append("The cobro cannot be empty")
    elif recoleccion["cobro"] < 0:
        errors.append("Te cobro cannto be 0")
    if not recoleccion["status"]:
        errors.append("The status cannot be empty")

    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))

 

async def recoleccion_update_validator(request: Request):
    errors = []
    recoleccion = await request.json()
    if not recoleccion["fecha"]:
        errors.append("The fech cannot be empty")
    if not recoleccion["lugar"]:
        errors.append("The lugar cannot be empty")
    if not recoleccion["id_cobro"]:
        errors.append("The id_cobro cannot be empty")
    if not recoleccion["cobro"]:
        errors.append("The cobro cannot be empty")
    elif recoleccion["cobro"] < 0:
        errors.append("Te cobro cannto be 0")
    if not recoleccion["status"]:
        errors.append("The status cannot be empty")

    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))