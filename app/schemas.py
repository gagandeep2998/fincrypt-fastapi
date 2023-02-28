from pydantic import BaseModel


class Card(BaseModel):
    card_number: str
    cvv: str
    expiry_month: str
    expiry_year: str
