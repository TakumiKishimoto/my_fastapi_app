from fastapi import FastAPI
from csv_upload import router as csv_router  # 追加

app = FastAPI()

app.include_router(csv_router)  # 追加

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def index():
#     return {"Hello": "World"}
