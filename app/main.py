from fastapi import FastAPI, APIRouter
from fastapi.testclient import TestClient
from app.routers import tablets
# from u_tests.products_tests import test_root


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

routerRoot = APIRouter()

@routerRoot.get("/")
def root():
    return {"message" : "Go to the url http://127.0.0.1:8000/docs to apply some requests"}
    
app.include_router(tablets.router)
app.include_router(routerRoot)

# client = TestClient(app)

# test_root(client)

