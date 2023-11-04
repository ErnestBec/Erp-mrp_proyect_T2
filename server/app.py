from fastapi import FastAPI
# import uvicorn
from fastapi import HTTPException
from routes.routes_user import user
from utils.appError_utils import http_error_handler, server_error_handler
from dotenv import load_dotenv
from routes.routes_products import product


app = FastAPI()
# Manejo de Errores
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, server_error_handler)

# load env
load_dotenv()

# Routes
app.include_router(user)
app.include_router(product)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
