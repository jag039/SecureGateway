from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
try:
    print("Trying to connect...")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1;"))
        print("WE ARE CONNECED, Result: ", result.fetchone())
except Exception as e:
    print("Failed to connect:", e)


load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")