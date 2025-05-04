from sqlalchemy.orm import Session
from app.models.tablet import Tablet
from app.schemas.tablets import TabletCreate, TabletUpdate
from app.utils.responses import ResponseHandler


class TabletCrud:
    
    @staticmethod
    def get_all_tablets(db: Session, page: int, limit: int, search = ""):
        tablets = db.query(Tablet).order_by(Tablet.id.asc()).filter(
            Tablet.name.contains(search)).limit(limit).offset((page - 1) * limit).all()
        
        return {"message": f"Page {page} with {limit} products", "data" : tablets}
    
    def get_tablet(db: Session, tablet_id: int):
        tablet = db.query(Tablet).filter(Tablet.id == tablet_id).first()
        if not tablet:
            ResponseHandler.not_found_error("Product", tablet_id)
            
        return ResponseHandler.get_single_success(tablet.name, tablet_id, tablet)
    
    @staticmethod
    def create_tablet(db: Session, tablet : TabletCreate):
        db_tablet = Tablet(id = None, **tablet.model_dump())
        db.add(db_tablet)
        db.commit()
        db.refresh(db_tablet)
        return ResponseHandler.create_success(db_tablet.name, db_tablet.id, db_tablet)
    
    @staticmethod
    def update_tablet(db : Session, tablet_id : int, updated_tablet: TabletUpdate):
        db_tablet = db.query(Tablet).filter(Tablet.id == tablet_id).first()
        
        if not db_tablet:
            ResponseHandler.not_found_error("Product", tablet_id)
            
        
        for key, value in updated_tablet.model_dump().items():
            setattr(db_tablet, key, value)
            
        db.commit()
        db.refresh(db_tablet)
        return ResponseHandler.update_sucess(db_tablet.name, db_tablet.id, db_tablet)
    
    @staticmethod
    def delete_tablet(db: Session, tablet_id : int):
        
        db_tablet = db.query(Tablet).filter(Tablet.id == tablet_id).first()
        
        if not db_tablet:
            ResponseHandler.not_found_error("Product", tablet_id)
            
        db.delete(db_tablet)
        db.commit()
        
        return ResponseHandler.delete_success(db_tablet.name, db_tablet.id, db_tablet)
    
            
        