from fastapi import APIRouter, Depends, HTTPException
from app.models.payment import TokenizeRequest
from sqlalchemy.orm import Session
from app.services.tokenization import tokenize_card
from app.database.db import get_db
from app.services.auth import get_current_user

router = APIRouter()
@router.post("/tokenize")
def tokenize(
    request: TokenizeRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user["role"] != "processor":
        raise HTTPException(status_code=403, detail="Not authorized")
    token = tokenize_card(request, db) 
    return {"token": token}