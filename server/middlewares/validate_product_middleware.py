from fastapi import Request, HTTPException


async def product_validate_middleware(request: Request):
    errors = []
    product = await request.json()
    if not product["name_prod"]:
        errors.append("The name cannot be empty")
    if not product["Descripcion"]:
        errors.append("The descripcion cannot be empty")
    if not product["min_stock"]:
        errors.append("The min_stock cannot be empty")
    elif product["min_stock"] < 10:
        errors.append("Te min_stock cannot be 10")
    if not product["max_stock"]:
        errors.append("The max_stock cannot be empty")
    elif product["max_stock"] < 100:
        errors.append("Te max_stock the must be between 100 and 10")
    if not product["precio_uni"]:
        errors.append("The precio_uni cannot be empty")
    elif product["precio_uni"] < 0:
        errors.append("Te precio_uni cannto be 0")
    if not product["mp"]:
        errors.append("The mp cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))


async def product_update_validator(request: Request):
    errors = []
    product = await request.json()
    if not product["name_prod"]:
        errors.append("The name cannot be empty")
    if not product["Descripcion"]:
        errors.append("The descripcion cannot be empty")
    if not product["min_stock"]:
        errors.append("The min_stock cannot be empty")
    elif product["min_stock"] <= 10:
        errors.append("Te min_stock cannot be 10")
    if not product["max_stock"]:
        errors.append("The max_stock cannot be empty")
    elif product["max_stock"] >= 100:
        errors.append("Te max_stock the must be between 100 and 10")
    elif product["max_stock"] < 10:
        errors.append("Te max_stock the must be between 100 and 10")
    if not product["precio_uni"]:
        errors.append("The precio_uni cannot be empty")
    elif product["precio_uni"] < 0:
        errors.append("Te precio_uni cannto be 0")
    if not product["num_pieza"]:
        errors.append("The num_pieza cannot be empty")
    if not product["cantidad_prod"]:
        errors.append("The cantidad cannot be empty")
    elif product["cantidad_prod"] < 0:
        errors.append("Te cantidad cannto be 0")
    if not product["mp"]:
        errors.append("The mp cannot be empty")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))


def products_exist(request: Request):
    print(request["products"])
