from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

x = 50

class Item(BaseModel):
    mile : int

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

@router.get('/list')

def listEx(limit:int):
    listArray  = list(range(1,limit))
    return listArray

@router.get('/dictionaries')

def getData():
    persons = {"Jeff": "Is afraid of clowns.", "David":" Plays the piano."}
    return persons

@router.get('/keys')

def getData():
    persons = {"Jeff": "Is afraid of clowns.", "David":" Plays the piano."}
    persons['Jeff'] = "He is a teacher"
    persons['henry'] = "New to town"    
    return persons

@router.get('/tuples')

# list of tuples
def getData():
    airports = [('bglr','123'),('chennai','456')]
    data = []
    for airport in airports:
        name = airport[0]
        code = airport[1]
        data.append({"name":name,"code":code})
        
    return data

# Functions Assignment
# - Create a function that takes in 3 parameters(firstname, lastname, age) and
# returns a dictionary based on those values

# http://localhost:8000/test?user=ananthy&id=1&email=sdd
@router.get('/test')

def getDict(user,id,email):
    return {"user":user,"id":id,"email":email}

