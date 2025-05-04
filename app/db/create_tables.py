from app.db.database import engine
from app.models.tablet import Tablet
from app.db.base import Base

Base.metadata.create_all(bind=engine)
