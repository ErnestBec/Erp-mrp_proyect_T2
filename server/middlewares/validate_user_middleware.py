from fastapi import Request, HTTPException


async def user_validate_middleware(request: Request):
    errors = []
    user = await request.json()
    if not user["name"]:
        errors.append("The name cannot be empty")
    if not user["email"]:
        errors.append("The email cannot be empty")
    elif not user["email"].count("@") == 1 or not user["email"].count(".") > 0:
        errors.append("Enter a valid email")
    if not user["password"]:
        errors.append("The password cannot be empty")
    elif not user["password"].isalnum():
        errors.append("The password must contain letters and numbers")
    elif len(user["password"]) < 8:
        errors.append("The password must contain at least 8 characters")
    if not user["phone"]:
        errors.append("The phone  number cannot be empty")
    elif len(str(user["phone"])) > 10:
        errors.append("The phone number can only contain 10 digits")
    elif len(str(user["phone"])) < 10:
        errors.append("The phone number can only contain 10 digits")
    if user["role"] != "client":
        if user["role"] != "admin":
            errors.append("The rol invalid")

    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))


async def user_update_validator(request: Request):
    errors = []
    user = await request.json()
    if not user["email"]:
        errors.append("The email cannot be empty")
    elif not user["email"].count("@") == 1 or not user["email"].count(".") > 0:
        errors.append("Enter a valid email")
    if not user["name"]:
        errors.append("The name cannot be empty")
    if not user["phone"]:
        errors.append("The phone  number cannot be empty")
    elif len(str(user["phone"])) > 10:
        errors.append("The phone number can only contain 10 digits")
    elif len(str(user["phone"])) < 10:
        errors.append("The phone number can only contain 10 digits")
    if errors:
        raise HTTPException(status_code=400, detail=". ".join(errors))
