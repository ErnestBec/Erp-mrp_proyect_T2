from fastapi import Request, HTTPException


async def RowMaterial_validate_middleware(request: Request):
    errors = []
    rawMat = await request.json()
    if not rawMat["tipo"]:
        errors.append("The tipo cannot be empty")
    if not rawMat["quantity"]:
        errors.append("The quantity cannot be empty")
    if not rawMat["min_stock"]:
        errors.append("The min_stock cannot be empty")
    if not rawMat["max_stock"]:
        errors.append("The max_stock_fabri be empty")
    elif rawMat["max_stock"] < 100:
        errors.append("Te max_stock cannot be 0")
    if not rawMat["id_space_Rack"]:
        errors.append("The id_space_Rack cannot by empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))

 

async def RowMaterial_update_validator(request: Request):
    errors = []
    rawMat = await request.json()
    if not rawMat["tipo"]:
        errors.append("The tipo cannot be empty")
    if not rawMat["quantity"]:
        errors.append("The quantity cannot be empty")
    if not rawMat["min_stock"]:
        errors.append("The min_stock cannot be empty")
    if not rawMat["max_stock"]:
        errors.append("The max_stock_fabri be empty")
    elif rawMat["max_stock"] < 100:
        errors.append("Te max_stock cannot be 0")
    if not rawMat["id_space_Rack"]:
        errors.append("The id_space_Rack cannot by empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))