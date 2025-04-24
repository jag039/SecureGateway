from fastapi import APIRouter, Depends, HTTPException
from app.models.payment import TokenizeRequest
from sqlalchemy.orm import Session
from app.services.tokenization import tokenize_card
from app.database.db import get_db
from app.services.auth import get_current_user
from app.logging_config import setup_logger

router = APIRouter()
logger = setup_logger()

@router.post("/tokenize")
def tokenize(
    request: TokenizeRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user["role"] != "processor":
        logger.warning({
            "event": "unauthorized_access",
            "path": "/tokenize",
            "sub": user.get("sub", "unknown"),
            "reason": "Role not processor",
            "status": 403
        })
        raise HTTPException(status_code=403, detail="Not authorized")
    
    token = tokenize_card(request, db) 
    logger.info({
        "event": "tokenization_success",
        "path": "/tokenize",
        "sub": user["sub"],
        "status": 200
    })
    
    return {"token": token}
