from fastapi import FastAPI
# import uvicorn
from fastapi import HTTPException
from routes.routes_user import user
from utils.appError_utils import http_error_handler, server_error_handler


app = FastAPI()
# Manejo de Errores
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, server_error_handler)


app.include_router(user)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
