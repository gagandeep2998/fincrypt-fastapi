from .. import schemas
from fastapi import APIRouter


router = APIRouter(
    prefix="/cards",
    tags=["Cards"]
)

@router.get("/")
def root():
    return {"message": "Welcome to Fincrypt"}


@router.post("/")
def add_card(new_card: schemas.Card):
    print(new_card)
    return new_card
