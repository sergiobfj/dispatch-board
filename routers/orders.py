from fastapi import APIRouter, Depends, File, UploadFile
from sqlmodel import Session, select
from models import OrderBase, Order
from database import get_session

from io import BytesIO
import openpyxl

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

@router.patch("/orders/{id}")
def update_order(id: int, status: str, session: Session = Depends(get_session)):

    order = session.get(Order, id)
    order.status = status

    session.add(order)
    session.commit()
    session.refresh(order)

    return order

@router.get("/orders")
def list_orders(session: Session = Depends(get_session)):
    
    statement = select(Order)
    orders = session.exec(statement).all()

    return{
        "orders": orders
    }

@router.post("/import")
async def import_orders(file: UploadFile, session: Session = Depends(get_session)):
    contents = await file.read()
    workbook = openpyxl.load_workbook(BytesIO(contents))
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        code, client_name, solar_panels_qty, modules, inverter, kit_tech, city, notes, roof_type = row

        order = Order(
            code = code,
            client_name = client_name,
            solar_panels_qty = solar_panels_qty,
            modules = modules,
            inverter = inverter,
            kit_tech = kit_tech,
            city = city,
            notes = notes,
            roof_type = roof_type
        )
    
        session.add(order)

    session.commit()
    return {
        "message": "Importado com sucesso"
    }