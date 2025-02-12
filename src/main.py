from apis.base import api_router
from clients.send_grid_client import send_email
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    # app.include_router(api_router)
    
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Hello Universe"}


@app.post("/test")
async def test_stuff():
    send_email({"a": "A"})
    return {"message": "..."}
