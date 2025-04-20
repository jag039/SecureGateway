from fastapi import FastAPI
from app.routes import payment 

app = FastAPI()
app.include_router(payment.router)

@app.get("/")
def health_check():
    return {"status": "up"}
