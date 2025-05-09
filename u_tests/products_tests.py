from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock
from app.schemas.tablets import TabletBase
from app.db.database import get_db

client = TestClient(app)

db_simulator = [
    TabletBase(name='VAIO', description='TL10', price=70.30, link='db_simulator/vaio-tl10', id = 1),
    TabletBase(name='Samsung', description='Galaxy Tab A8', price=120.00, link='db_simulator/samsung-a8', id = 2),
    TabletBase(name='Apple', description='iPad 9ª Geração', price=329.99, link='db_simulator/ipad9', id = 3),
    TabletBase(name='Lenovo', description='Tab M10', price=110.50, link='db_simulator/lenovo-m10', id = 4),
    TabletBase(name='Xiaomi', description='Pad 5', price=289.90, link='db_simulator/xiaomi-pad5', id = 5),
    TabletBase(name='Asus', description='ZenPad 3S 10', price=199.99, link='db_simulator/asus-zenpad', id = 6),
    TabletBase(name='Multilaser', description='M8 NB348', price=89.00, link='db_simulator/multilaser-m8', id = 7),
    TabletBase(name='Amazon', description='Fire HD 10', price=149.99, link='db_simulator/amazon-fire10', id = 8),
    TabletBase(name='Huawei', description='MatePad T10', price=139.90, link='db_simulator/huawei-t10', id = 9),
    TabletBase(name='Alldocube', description='iPlay 40 Pro', price=169.50, link='db_simulator/alldocube-iplay', id = 10)
]

def get_db_simulator():
    
    db = MagicMock()
    query_mock = MagicMock()
    query_mock.all.return_value = db_simulator
    db.query.return_value =  query_mock
    return db

app.dependency_overrides[get_db] = get_db_simulator


def test_get_tablets_simulator(client):
    response = client.get("tablets/simulator-tablets/")
    assert response.status_code == 200

    expected = [tablet.model_dump() for tablet in db_simulator]
    response_data = response.json()["data"]  

    assert response_data == expected
    print("Status 200: OK")



def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    print("Status 200: OK")
    
def test_get_item_by_id(client, id):
    
    response = client.get(f"/tablets/{id}")
    ident = response.json()['data']['id']
    
    
    assert response.status_code == 200
    assert ident == id
    
    print("Status 200: OK")

def test_create_item(client):
    
    response = client.post(
        "/tablets/",
        json = {"name" : "Multilaser", "description" : "K10 V-T", "price" : 112.5, "link" : "tablets/"})
    
    assert response.status_code == 201
    
    data = response.json()['data']
    idData = data['id']
        
    assert data == {
            "name" : "Multilaser",
            "description" : "K10 V-T",
             "price" : 112.5,
             "link" : "tablets/",
             "id" : idData      
     }
    
    print(data)
    print("Status 201: OK")
    
    

def test_update_item(client, id, name, description, price, link):
       
        response = client.put(
        f'/tablets/{id}',
        json = {"name" : name, "description" : description, "price" : price, "link" : link}
        )
        
        assert response.status_code == 200
        
def test_delete_item(client, id):
    
    response = client.delete(
        f'tablets/{id}'
    )
    
    assert response.status_code == 200
    
    print('Status 200: OK')
    

test_get_tablets_simulator(client)
    


   
    
    
