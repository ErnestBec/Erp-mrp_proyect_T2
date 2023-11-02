from fastapi import FastAPI
# import uvicorn
from routes.routes_user import user


app = FastAPI()


app.include_router(user)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
