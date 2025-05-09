from sqlalchemy import create_engine
from app.crud.tablets import TabletCrud
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings
from app.models.tablet import Tablet
from app.db.base import Base

engine = create_engine(settings.DATABASE_URL, connect_args= {"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

def get_db():
    
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
        
def create_item(tablet):
    db_generator = get_db()
    db = next(db_generator)
    
    try:
        TabletCrud.create_tablet(db, tablet)
    finally:
        db.close()
        
def delete_item(id):
    db_generator = get_db()
    db = next(db_generator)
    
    try:
        TabletCrud.delete_tablet(db, id)
        
    finally:
        db.close()
    
def drop_all():
    
  Base.metadata.drop_all(engine)