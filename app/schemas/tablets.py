from pydantic import BaseModel, root_validator
from typing import List

class BaseConfig:
    from_attributes = True
    
class TabletBase(BaseModel):
    
    name : str
    description : str
    price : float
    link : str 
    id : int
    
    class Config(BaseConfig):
        pass
    
        
class TabletCreate(BaseModel):
    
    name : str
    description : str
    price : float
    link : str
    
    
    
    class Config(BaseConfig):
        pass
        
class TabletUpdate(TabletCreate):
    pass

class TabletGet(BaseModel):
    
    message : str
    data : TabletBase
    
    class Config(BaseConfig):
        pass
    
class TabletsGet(BaseModel):
    
    message : str
    data : List[TabletBase]
    
    class Config(BaseConfig):
        pass
    
class TabletDelete(TabletBase):
    pass

class TabletDeletedGet(BaseModel):
    message : str
    data : TabletDelete