from fastapi import Request, HTTPException


async def RowMaterial_validate_middleware(request: Request):
    errors = []
    rawMat = await request.json()
    if not rawMat["Name"]:
        errors.append("The name cannot be empty")
    if not rawMat["min_stock"]:
        errors.append("The min_stock cannot be empty")
    if not rawMat["max_stock"]:
        errors.append("The max_stock_fabri be empty")
    elif rawMat["max_stock"] < 100:
        errors.append("Te max_stock cannot be 0")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))


async def RowMaterial_update_validator(request: Request):
    errors = []
    rawMat = await request.json()
    if not rawMat["Name"]:
        errors.append("The name cannot be empty")
    if not rawMat["min_stock"]:
        errors.append("The min_stock cannot be empty")
    if not rawMat["max_stock"]:
        errors.append("The max_stock_fabri be empty")
    elif rawMat["max_stock"] < 100:
        errors.append("Te max_stock cannot be 0")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))
