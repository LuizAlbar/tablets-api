from app.db.database import engine
from app.models.tablet import Tablet
from app.db.base import Base
from app.db.database import create_item, delete_item, drop_all
from app.scraper.product_scraper import listOfTablets, get_product
from app.schemas.tablets import TabletCreate
from app.crud.tablets import TabletCrud



#create database with the table Tablet
Base.metadata.create_all(bind=engine)

singleTablet = TabletCreate(name="Iphone", description="15", price=800.5, link="iphone.com")

for index, tablet in enumerate(listOfTablets):
    
    tablet = get_product(listOfTablets[index])
    
    name = tablet['name']
    description = tablet['description']
    price = tablet['price']
    link = tablet['link']

    newTablet = TabletCreate(name= name, description= description, price= price, link= link)
    
    #Tablets already added into the database
    create_item(newTablet)
    
    








