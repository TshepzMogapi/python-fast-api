import logging
from fastapi import FastAPI

app = FastAPI()

@app.get("/notify", status_code=200)
def send_notifications():
    logging.info("Sending Notifications")