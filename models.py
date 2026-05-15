from sqlmodel import SQLModel, Field
from datetime import datetime

class OrderBase(SQLModel):
    client_name: str
    solar_panels_qty: int
    route: str
    product_type: str
    status: str = Field(default="waiting")

class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)