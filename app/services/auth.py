from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt
import os


load_dotenv()
JWT_KEY = os.getenv("JWT_KEY")
security = HTTPBearer()

def encode_jwt(payload: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = payload.copy()
    to_encode["exp"] = datetime.utcnow() + expires_delta

    return jwt.encode(payload, JWT_KEY, algorithm="HS256")

def decode_jwt(encoded: str):
    return jwt.decode(encoded, JWT_KEY, algorithms="HS256")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    scheme = credentials.scheme
    if scheme != "Bearer":
        raise HTTPException(status_code=403, detail="Permission Not Granted")
    try:
        decoded = decode_jwt(token)
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token expired")