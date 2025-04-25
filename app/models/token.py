from sqlalchemy import Column, Integer, String, DateTime
from app.database.db import Base
from datetime import datetime


class TokenizedData(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String(), unique=True, nullable=False)
    encrypted_data = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
