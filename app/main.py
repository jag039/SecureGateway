from fastapi import FastAPI
from app.routes import payment
from app.logging_config import setup_logger
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.include_router(payment.router)
logger = setup_logger()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


@app.get("/")
def health_check():
    return {"status": "up"}
