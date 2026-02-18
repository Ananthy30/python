from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel

realRouter = APIRouter()

books = [
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
  },
  {
    "id": 3,
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt & David Thomas",
    "genre": "Technology"
  },
  {
    "id": 4,
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self-Help",
  }
]

class bookObj(BaseModel):
  id: int
  title: str
  author: str
  genre: str

@realRouter.get('/read_books')

def read_books():
    return books

# dynamic param - path param
@realRouter.get('/read_books/{book_title}')

async def getBook(book_title : str):
    for book in books:
     if(book['title'] == book_title):
         return book
       
# this is a post
@realRouter.post('/add')
# this book is a request body
def addBook(book:bookObj):
  books.append(book)
  return books

# this is a put
@realRouter.put('/books/update')

def updateBook(bookItem:bookObj):
  for index,book in enumerate(books):
    if book.get('id') == bookItem.id:
      books[index] = bookItem
    return books

# this is a delete
@realRouter.delete('/books/delete/{id}')

def deleteBook(id:int):
  for index,book in enumerate(books):
    if book.get('id') == id:
     books.pop(index)
     break
  
  return books
     
