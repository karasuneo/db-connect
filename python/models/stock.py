from typing import Optional
from sqlmodel import Field, SQLModel
from settings import get_db_engine

class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    refrigerator_id: int
    stock_name: str
    quantity: str
    stock_image: str
    expiration_date: str
    
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=get_db_engine())  