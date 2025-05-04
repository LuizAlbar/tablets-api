from fastapi import FastAPI
from app.routers import tablets

app = FastAPI(
    
    description= "Tablet e-commerce API",
    title= "Tablets API",
    contact={
        "name": "LuizAlbar",
        "url": "https://github.com/LuizAlbar"   
    },
    swagger_ui_parameters= {
        
        "syntaxHighlight.theme" : "monokai",
        "layout" : "BaseLayout",
        "filter" : True,
        "tryItOutEnabled" : True,
        "onComplete" : "Ok"
    },
)

app.include_router(tablets.router)