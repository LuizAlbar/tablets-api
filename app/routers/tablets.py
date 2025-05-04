from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.crud.tablets import TabletCrud
from sqlalchemy.orm import Session
from app.schemas.tablets import TabletCreate, TabletUpdate, TabletGet, TabletsGet

router =  APIRouter(tags= ['Tablets'], prefix= "/tablets")

@router.get("/", status_code=status.HTTP_200_OK, response_model= TabletsGet)
def get_all_tablets(
    db: Session = Depends(get_db),
    page: int = Query(1, ge= 1, description= "Page number"),
    limit : int = Query(10, ge= 1, le=100, description= "Items per page"),
    search : str | None = Query("", description= "Search based title of products")
):
    return TabletCrud.get_all_tablets(db, page, limit, search)