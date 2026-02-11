from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

x = 50

class Item(BaseModel):
    mile : int

@router.get('/one')

def oneDay():
    return x

@router.get('/permonth')

def perMonth():
    return 30*x

@router.get('/how')

def returnMode(mile : int):
    if mile < 5:
        return 'walk'
    elif mile > 100:
        return 'fly'
    else:
        return 'figure out dont ask'
    
@router.get('/find')

def find():
    animals = ['cat','dog','bear']
    try:
     animals.find('lion')
     return 'found lion'
    except:
     return 'no animals found'
    
