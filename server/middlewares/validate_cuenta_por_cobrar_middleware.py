from fastapi import Request, HTTPException


async def ceuenta_por_cobrar_validate_middleware(request: Request):
    errors = []
    cuenta = await request.json()
    if not cuenta["solicitud"]:
        errors.append("The name cannot be empty")
    if not cuenta["importe"]:
        errors.append("The import cannot be empty")
    elif cuenta["importe"] <= 100:
        errors.append("Te min_stok cannot be 10")
    if not cuenta["fecha_emision"]:
        errors.append("The fecha_emision cannot be empty")
    if not cuenta["total"]:
        errors.append("The total cannot be empty")
    elif cuenta["total"] < 0:
        errors.append("Te total cannto be 0")
    if not cuenta["fecha_de_pago"]:
        errors.append("The num_pieza cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))

 

async def cuenta_por_cobrar_update_validator(request: Request):
    errors = []
    cuenta = await request.json()
    if not cuenta["solicitud"]:
        errors.append("The name cannot be empty")
    if not cuenta["importe"]:
        errors.append("The import cannot be empty")
    elif cuenta["importe"] <= 100:
        errors.append("Te min_stok cannot be 10")
    if not cuenta["fecha_emision"]:
        errors.append("The fecha_emision cannot be empty")
    if not cuenta["total"]:
        errors.append("The total cannot be empty")
    elif cuenta["total"] < 0:
        errors.append("Te total cannto be 0")
    if not cuenta["fecha_de_pago"]:
        errors.append("The num_pieza cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))