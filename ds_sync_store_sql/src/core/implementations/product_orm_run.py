from sqlalchemy import Column, Integer, String, Float
from src.core.contracts.db_declarative_contract import Base

class ProductORM(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
