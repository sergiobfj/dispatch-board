from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models import OrderBase, Order
from database import get_session

router = APIRouter()

@router.post("/orders")
def create_order(order: OrderBase, session: Session = Depends(get_session)):

    db_order = Order.model_validate(order)

    session.add(db_order) # adiciona na fila
    session.commit() # grava no banco
    session.refresh(db_order) # atualiza o objeto com o ID gerado
    return db_order

@router.get("/display")
def get_display(session: Session = Depends(get_session)):

    # queries de filtrando por status:
    
    statement = select(Order).where(Order.status == "in_progress")
    in_progress = session.exec(statement).first()

    statement = select(Order).where(Order.status == 'waiting')
    next_order = session.exec(statement).first()

    statement = select(Order).where(Order.status == "completed")
    previous = session.exec(statement).all() 

    return {
        "in_progress": in_progress,
        "next": next_order,
        "previous": previous
    }