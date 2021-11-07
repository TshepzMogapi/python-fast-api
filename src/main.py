from apis.base import api_router
from clients.send_grid_client import send_email
from core.config import settings
from fastapi import FastAPI

# from db.base import Base
# from db.session import engine


# def create_tables():
#     Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    # include_router(app)
    # create_tables()
    return app


app = start_application()
# app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Universe"}


@app.post("/test")
async def test_stuff():
    send_email({"a": "A"})
    return {"message": "..."}
