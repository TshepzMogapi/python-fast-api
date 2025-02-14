from apis.base import api_router
from clients.send_grid_client import send_email
from core.config import *
from db.base import Base
from db.session import engine
from fastapi import FastAPI

def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI()
    # app.include_router(api_router)
    
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": f"Hello, {settings.PROJECT_DESCRIPTION}"}
