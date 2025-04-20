from pydantic import BaseModel, Field

class TokenizeRequest(BaseModel):
    card_number: str = Field(..., min_length=12, max_length=19, example="4111111111111111")
    cvv: str = Field(..., min_length=3, max_length=4, example="123")
    expiry: str = Field(..., regex=r"^(0[1-9]|1[0-2])/\d{2}$", example="04/26")