from fastapi import Request, HTTPException


async def ceuenta_Pagar_validate_middleware(request: Request):
    errors = []
    cuenta = await request.json()
    if not cuenta["proveedor"]:
        errors.append("The proveedor cannot be empty")
    if not cuenta["solicitud"]:
        errors.append("The solicitud cannot be empty")
    elif cuenta["importe"] <= 100:
        errors.append("Te min_stok cannot be 10")
    if not cuenta["total"]:
        errors.append("The total cannot be empty")
    elif cuenta["total"] < 0:
        errors.append("Te total cannto be 0")
    if not cuenta["fecha_de_pago"]:
        errors.append("The num_pieza cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))

 

async def cuenta_Pagar_update_validator(request: Request):
    errors = []
    cuenta = await request.json()
    if not cuenta["proveedor"]:
        errors.append("The proveedor cannot be empty")
    if not cuenta["solicitud"]:
        errors.append("The solicitud cannot be empty")
    elif cuenta["importe"] <= 100:
        errors.append("Te min_stok cannot be 10")
    if not cuenta["total"]:
        errors.append("The total cannot be empty")
    elif cuenta["total"] < 0:
        errors.append("Te total cannto be 0")
    if not cuenta["fecha_de_pago"]:
        errors.append("The num_pieza cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))