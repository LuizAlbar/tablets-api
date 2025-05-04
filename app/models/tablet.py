from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import Base

class Tablet(Base):
    
    __tablename__ = 'tablets'
    
    name = Column(String(25), nullable = False)
    description = Column(String(100), nullable= False)
    price = Column(Float(7), nullable= False)
    link = Column(String, nullable= False)
    id = Column(Integer, primary_key= True, unique= True, index= True, nullable= False, autoincrement= True)
    
    