from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.crud.tablets import TabletCrud
from sqlalchemy.orm import Session
from app.schemas.tablets import TabletCreate, TabletUpdate, TabletGet, TabletsGet, TabletDeletedGet, TabletBase

router =  APIRouter(tags= ['Tablets'], prefix= "/tablets")

@router.get("/", status_code=status.HTTP_200_OK, response_model= TabletsGet)
def get_all_tablets(
    db: Session = Depends(get_db),
    page: int = Query(1, ge= 1, description= "Page number"),
    limit : int = Query(10, ge= 1, le=100, description= "Items per page"),
    search : str | None = Query("", description= "Search based title of products")
):
    return TabletCrud.get_all_tablets(db, page, limit, search)

@router.get("/{tablet_id}", status_code=status.HTTP_200_OK, response_model= TabletGet)
def get_tablet(tablet_id : int, db : Session = Depends(get_db)):
    return TabletCrud.get_tablet(db, tablet_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= TabletGet)
def create_tablet(
    tablet : TabletCreate,
    db : Session = Depends(get_db)):
    return TabletCrud.create_tablet(db, tablet)

@router.put(
    "/{tablet_id}",
    status_code=status.HTTP_200_OK,
    response_model= TabletGet)
def update_tablet(
    tablet_id : int,
    updated_tablet : TabletUpdate,
    db : Session = Depends(get_db)):
    
    return TabletCrud.update_tablet(db, tablet_id, updated_tablet)

@router.delete(
    "/{tablet_id}",
    status_code=status.HTTP_200_OK,
    response_model= TabletDeletedGet)
def delete_tablet(
    tablet_id : int,
    db : Session = Depends(get_db)):
    return TabletCrud.delete_tablet(db, tablet_id)

@router.get("/simulator-tablets/", response_model=TabletsGet)
def get_simulated_tablets(db: Session = Depends(get_db)):
    tablets = db.query(TabletGet).all()
    return {"message": "Success", "data": tablets}