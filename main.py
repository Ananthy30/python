from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel 
from exer import router

app = FastAPI()
app.include_router(router)

class Item(BaseModel):
    name: str
    price:int
    instock : Union[bool,None] = None
    
@app.get('/')

def root_fun():
    version = 3
    x = "I think "+ str(version)
    return x

@app.get('/items/{item_id}')

def root_items(item_id:int,a:Union[int, None] = 1):
    print("hello")
    return {"a" : item_id ,"b" : a}

@app.put('/items/{item_id}')

def putItem(item_id:int, item:Item):
    return {"id" : item_id ,"name" : item.name.title() + ' ' + "kdkk", "price": item.price }
    
