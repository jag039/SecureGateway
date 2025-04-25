from cryptography.fernet import Fernet
from app.models.payment import TokenizeRequest
from app.models.token import TokenizedData
import uuid
from dotenv import load_dotenv
import os

load_dotenv()
FERNET_KEY = os.getenv("FERNET_KEY")
f = Fernet(FERNET_KEY)


def tokenize_card(request: TokenizeRequest, db):
    token = str(uuid.uuid4())
    combined = f"{request.card_number}|{request.cvv}|{request.expiry}"
    encrypted_data = f.encrypt(combined.encode()).decode()

    record = TokenizedData(token=token, encrypted_data=encrypted_data)
    db.add(record)
    db.commit()
    db.refresh(record)

    return token
