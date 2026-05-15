from fastapi import APIRouter, Depends
from sqlmodel import Session
from models import OrderBase, Order
from database import get_session

router = APIRouter()

@router.post("/orders")
def create_order(order: OrderBase, session: Session = Depends(get_session)):
    db_order = Order.model_validate(order)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order